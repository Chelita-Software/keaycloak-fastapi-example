# Keycloak - Fast API Implementation example

1. Run `docker-compose up keycloak`

2. Modify /etc/hosts by adding:

```
127.0.0.1   keycloak
```

3. Navigate to keycloak server on http://keycloak:8080

4. Create new realm, client and user (set a password).

5. Add your client data to .env file in the root of this repo:

```
OPEN_ID_CLIENT_ID=xxx
OPEN_ID_CLIENT_SECRET=xxx-xxx-xxx
````

6. Run `docker-compose up` to start the python app and navigate to http://localhost:8001/login

7. Congrats, you login in fastapi using keycloak
