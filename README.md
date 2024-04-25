# MASTER-DJANGO-TASK

**Autor**: Javier Llinares

**Comentarios**: Para simplicidad de la tarea los metodos no se les coloco tokens de seguridad Bearer a las peticiones.


------------

### Proyecto y Dockerizacion

Se anexa la evidencias que el proyecto se ejecuta con sus correspondientes contenedores

![Imagen compose](images/Evidencias-Compose.png?raw=true)

![Imagen docker](images/Evidencia-Docker-Desk.png?raw=true)

![Imagen swagger](images/Evidencia-Swagger.png?raw=true)


------------

### Pruebas Unitarias

Se construyeron pruebas unitarias basicas tanto al modelo generado como a los APIs expuesto, las clases correspondientes son:

- test_models.py
- test_client_api.py

![Imagen pruebas](images/Evidencias-Pruebas-Unitarias.png?raw=true)

------------

### Pruebas Postman

**Path base del API**: http://127.0.0.1:8000/api/clients/client/


------------


**Prueba de Listado de clientes (GET):** http://127.0.0.1:8000/api/clients/client/

**Data de prueba:**
curl --location 'http://127.0.0.1:8000/api/clients/client/' \
--header 'Accept: application/json' 

![Imagen pruebas](images/Prueba-Lista-Cliente.png?raw=true)

------------
**Prueba de creación de cliente (POST):** http://127.0.0.1:8000/api/clients/client/

**Data de prueba:**
curl --location 'http://127.0.0.1:8000/api/clients/client/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Accept: application/json' \
--data-urlencode 'country=ARGENTINA' \
--data-urlencode 'first_name=Nombre Postman' \
--data-urlencode 'last_name=Apellido Postman' \
--data-urlencode 'active=true'

![Imagen pruebas](images/Prueba-Crear-Cliente.png?raw=true)

------------

**Prueba de consulta de cliente por su ID (GET):** http://127.0.0.1:8000/api/clients/client/{id}

**Data de prueba:**
curl --location 'http://127.0.0.1:8000/api/clients/client/37/' \
--header 'Accept: application/json' 

![Imagen pruebas](images/Prueba-Crear-Cliente-ID.png?raw=true)

------------

**Prueba de actualizacion total de cliente por su ID (PUT):** http://127.0.0.1:8000/api/clients/client/{id}

**Data de prueba:**
curl --location --request PUT 'http://127.0.0.1:8000/api/clients/client/37/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Accept: application/json' \
--data-urlencode 'country=ARGENTINA 2' \
--data-urlencode 'first_name=POSTMAN 2' \
--data-urlencode 'last_name=POSTMANT 2' \
--data-urlencode 'active=false'

![Imagen pruebas](images/Prueba-Actualizar-Cliente.png?raw=true)

------------

**Prueba de actualizacion parcial de cliente por su ID (PATCH):** http://127.0.0.1:8000/api/clients/client/{id}

**Data de prueba:**
curl --location --request PATCH 'http://127.0.0.1:8000/api/clients/client/37/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Accept: application/json' \
--data-urlencode 'first_name=ACTUALIZACION PARCIAL'

![Imagen pruebas](images/Prueba-Actualizar-Parcial-Cliente.png?raw=true)

------------

**Prueba de borrado de cliente por su ID (DELETE):** http://127.0.0.1:8000/api/clients/client/{id}
**Data de prueba:**
curl --location --request DELETE 'http://127.0.0.1:8000/api/clients/client/37/' \

![Imagen pruebas](images/Prueba-Borrar-Cliente.png?raw=true)


------------
