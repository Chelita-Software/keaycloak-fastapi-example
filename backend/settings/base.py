import os


OPEN_ID_CLIENT_ID = os.getenv('OPEN_ID_CLIENT_ID')
OPEN_ID_CLIENT_SECRET = os.getenv('OPEN_ID_CLIENT_SECRET')
OPEN_ID_SERVER_URL = "http://keycloak:8080"
OPEN_ID_REALM = "fast-api"
OPEN_ID_CALLBACK_URL = "http://fast-api:8001/auth/callback"
FRONTEND_HOME_URL = "http://fast-api:3000/home"