# Keycloak - Fast API Implementation example

This is an example of how to integrate Keycloak Auth Server with an app using FastAPI for backend and Next JS in client mode for frontend.

We follow the OAuth Security recomendations using a session cookie to store the token, so it is not exposed in frontend.

## How to run the example

1. Run `docker-compose up keycloak`

2. Modify /etc/hosts by adding:

```
127.0.0.1   keycloak
127.0.0.1   fast-api
```

3. Navigate to keycloak server on http://keycloak:8080

4. Create new realm, client and user (set a password).

5. Add your client data to .env file in the root of this repo:

```
OPEN_ID_CLIENT_ID=xxx
OPEN_ID_CLIENT_SECRET=xxx-xxx-xxx
````

6. Run `docker-compose up` to start the backend and frontend apps and navigate to http:/fast-api:3000/login

7. Click the login button

8. Congrats, you logged-in using keycloak and fast-api
