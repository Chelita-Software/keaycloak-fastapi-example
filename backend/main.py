from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from keycloak.exceptions import KeycloakOperationError

from backend.settings.base import FRONTEND_LOGIN_URL, FRONTEND_HOME_URL, OPEN_ID_CALLBACK_URL
from backend.utils.auth import keycloak_openid
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
    return request.user # This will return the user object from the middleware


@app.get("/auth/login")
async def login():
    auth_url = keycloak_openid.auth_url(
        redirect_uri=OPEN_ID_CALLBACK_URL,
        scope="openid",
        state="12345"
    )
    return RedirectResponse(auth_url)


@app.get("/auth/callback")
async def callback(code: str, state: str, response: Response):
    try:
        token = keycloak_openid.token(
            grant_type='authorization_code',
            code=code,
            redirect_uri=OPEN_ID_CALLBACK_URL,
        )
        keycloak_openid.userinfo(token['access_token'])
    except KeycloakOperationError as e:       
        return {"error": "Authentication error", "status": e.response_code, "message": e.error_message}
    except Exception as e:
        return RedirectResponse(url="/auth/login")
    response = RedirectResponse(url=FRONTEND_HOME_URL)
    response.set_cookie(key="session-x" , value=token['access_token'], httponly=True)
    response.set_cookie(key="session-refresh-x", value=token['refresh_token'], httponly=True)
    return response


@app.get("/auth/logout")
async def logout(request: Request, response: Response):
    refresh_token = request.cookies.get("session-refresh-x")
    keycloak_openid.logout(refresh_token)
    response = RedirectResponse(url=FRONTEND_LOGIN_URL)
    response.delete_cookie("session-x")
    response.delete_cookie("session-refresh-x")
    return response


@app.get("/auth/verify")
async def verify(request: Request):
    token = request.cookies.get("session-x")
    try:
        user = keycloak_openid.userinfo(token)
    except Exception as e:
        return JSONResponse(status_code=401, content={"error": "Authentication error", "message": "Unauthorized"})
    return user
