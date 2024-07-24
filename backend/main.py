from fastapi import FastAPI, Response, Request
from fastapi.responses import RedirectResponse
from keycloak.exceptions import KeycloakOperationError

from backend.settings.base import OPEN_ID_CALLBACK_URL
from backend.utils.auth import keycloak_openid
from backend.utils.middleware import AuthorizationMiddleware


app = FastAPI()
app.add_middleware(AuthorizationMiddleware)


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
    response = RedirectResponse(url="/priv/home")
    response.set_cookie(key="session-x" , value=token['access_token'])
    return response
