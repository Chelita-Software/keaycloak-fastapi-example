from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from keycloak import KeycloakOpenID

from backend.settings.base import OPEN_ID_CLIENT_ID, OPEN_ID_CLIENT_SECRET, OPEN_ID_SERVER_URL, OPEN_ID_REALM, OPEN_ID_CALLBACK_URL


app = FastAPI()

keycloak_openid = KeycloakOpenID(
    server_url=OPEN_ID_SERVER_URL,
    client_id=OPEN_ID_CLIENT_ID,
    realm_name=OPEN_ID_REALM,
    client_secret_key=OPEN_ID_CLIENT_SECRET,
)


@app.get("/home")
async def home():
    return {"message": "Welcome to the home page!"}


@app.get("/login")
async def login():
    auth_url = keycloak_openid.auth_url(
        redirect_uri=OPEN_ID_CALLBACK_URL,
        scope="openid",
        state="12345"
    )
    return RedirectResponse(auth_url)


@app.get("/callback")
async def callback(code: str, state: str):
    print(state)
    token = keycloak_openid.token(
        grant_type='authorization_code',
        code=code,
        redirect_uri="http://localhost:8001/callback",
    )
    user_info = keycloak_openid.userinfo(token['access_token'])
    return user_info
