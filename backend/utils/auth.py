from keycloak import KeycloakOpenID

from backend.settings.base import OPEN_ID_CLIENT_ID, OPEN_ID_CLIENT_SECRET, OPEN_ID_SERVER_URL, OPEN_ID_REALM


keycloak_openid = KeycloakOpenID(
    server_url=OPEN_ID_SERVER_URL,
    client_id=OPEN_ID_CLIENT_ID,
    realm_name=OPEN_ID_REALM,
    client_secret_key=OPEN_ID_CLIENT_SECRET,
)
