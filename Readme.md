Keycloak - Fast API Ejemplo de implementación

1 Ejecuta docker-compose up keycloak

2 Modifica tu /etc/hosts y agrega
127.0.0.1   keycloak

3 Navega hacia tu instancia de keycloak en http://keycloak:8080

4 Crea un nuevo realm, un cliente y un usuario con contraseña

5 Agrega los datos de tu cliente a un .env en la raíz de este archivo

OPEN_ID_CLIENT_ID=xxx
OPEN_ID_CLIENT_SECRET=xxx-xxx-xxx

6 Ejecuta Docker-compose up de nuevo para iniciar la app y navega hacia http://localhost:8001/login

7 Felicidades, iniciaste sesión en fastapi usando keycloak