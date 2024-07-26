import secrets
import uuid

from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from keycloak.exceptions import KeycloakOperationError

from backend.settings.base import FRONTEND_LOGIN_URL, FRONTEND_HOME_URL, OPEN_ID_CALLBACK_URL
from backend.utils.auth import keycloak_openid
from backend.utils.encrypt import CookieEncrypter
from backend.utils.middleware import AuthorizationMiddleware


app = FastAPI()
app.add_middleware(AuthorizationMiddleware)

origins = [
    "http://fast-api:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/priv/home")
async def home(request: Request):
    return request.user  # This will return the user object from the middleware


@app.get("/auth/login")
async def login():
    state = secrets.token_urlsafe(16)
    auth_url = keycloak_openid.auth_url(
        redirect_uri=OPEN_ID_CALLBACK_URL,
        scope="openid",
        state=state  # This is used to prevent CSRF attacks
    )
    response = RedirectResponse(auth_url)
    session_state_x = CookieEncrypter.encrypt(state)
    response.set_cookie(key="session-state-x",
                        value=session_state_x, httponly=True)
    return response


@app.get("/auth/callback")
async def callback(code: str, state: str, request: Request, response: Response):
    session_state_x = request.cookies.get("session-state-x")
    state_from_session = CookieEncrypter.decrypt(session_state_x)
    if state != state_from_session:  # Validate the session comes from the same user
        return JSONResponse(status_code=401, content={"error": "Authentication error", "message": "Invalid state"})
    try:
        token = keycloak_openid.token(
            grant_type='authorization_code',
            code=code,
            redirect_uri=OPEN_ID_CALLBACK_URL,
        )
        keycloak_openid.userinfo(token['access_token'])
    except KeycloakOperationError as e:
        return JSONResponse(status_code=401, content={"error": "Authentication error", "message": e.error_message})
    except Exception as e:
        return RedirectResponse(url="/auth/login")
    response = RedirectResponse(url=FRONTEND_HOME_URL)
    session_x = CookieEncrypter.encrypt(token['access_token'])
    session_refresh_x = CookieEncrypter.encrypt(token['refresh_token'])
    response.set_cookie(key="session-x", value=session_x, httponly=True)
    response.set_cookie(key="session-refresh-x",
                        value=session_refresh_x, httponly=True)
    return response


@app.get("/auth/logout")
async def logout(request: Request, response: Response):
    session_refresh_x = request.cookies.get("session-refresh-x")
    refresh_token = CookieEncrypter.decrypt(session_refresh_x)
    keycloak_openid.logout(refresh_token)
    response = RedirectResponse(url=FRONTEND_LOGIN_URL)
    response.delete_cookie("session-x")
    response.delete_cookie("session-refresh-x")
    return response


@app.get("/auth/verify")
async def verify(request: Request):
    session_x = request.cookies.get("session-x")
    token = CookieEncrypter.decrypt(session_x)
    try:
        user = keycloak_openid.userinfo(token)
    except Exception as e:
        return JSONResponse(status_code=401, content={"error": "Authentication error", "message": "Unauthorized"})
    return user
