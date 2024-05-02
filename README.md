# Globant-Challenge-Flask-Python-SQLITE
Globant’s Data Engineering Coding Challenge
Este proyecto resuelve el desafío de codificación de Ingeniería de Datos de Globant. Consiste en una aplicación Flask que maneja la migración de datos desde archivos CSV a una base de datos SQLite y proporciona métricas específicas sobre los datos migrados.

**Tecnologías Utilizadas**
Python
Flask
SQLite
Pandas
HTML/CSS
Docker

**Estructura del Proyecto**
app.py: Archivo principal que inicia la aplicación Flask y maneja las rutas.
controller_db.py: Contiene los métodos para la creación de tablas en la base de datos y la inserción de datos desde archivos CSV.
templates/: Carpeta que contiene los archivos HTML para las vistas.
static/: Carpeta que contiene archivos estáticos como CSS.
files_csv/: Carpeta que contiene los archivos CSV necesarios para la migración de datos.
requirements.txt: Archivo que lista las dependencias del proyecto.

**Características del Desafío ( está compuesto de 2 partes):**
Section 1: API
Se busca construir una API desde la cual se puedan cargar y migrar a una base de datos los datos contenidos en archivos CSV. Archivos CSV: 'departments', 'jobs' y 'hired_employees'. Se deben cumplir algunos requisitos: Ser capaz de insertar transacciones por lotes (de 1 a 1000 filas) con una sola solicitud y la base de datos debe ser SQL.
Section 2: SQL
Se quieren obtener algunas métricas de recursos humanos como empleados contratados por trimestre y departamentos con altas contrataciones.

**Configuración mediante Docker:**
Navegue hasta el directorio raíz.
Construya y ejecute la imagen Docker:
docker --build -t flask-app
docker run -p 7000:5000 flask-app

**Configuración manual:**
Navegue hasta el directorio raíz
Instale todas las bibliotecas en el requirements.txt
Navega al directorio /app/
Ejecuta app.py
La aplicación estará disponible en http://localhost:7000

**Uso de la API**
La aplicación inicia presentando el desafío, con la siguiente vista:
![1](https://github.com/yadelisgv/Globant-Challenge-Flask-Python-SQLITE/assets/40398052/9c0260c3-8410-457d-b009-53f1dda1d762)
La aplicación inicia con una vista que presenta el desafío propuesto y dos botones que nos llevan a cada una de las partes del desafío:

1. Carga de Archivos CSV y Migración de Datos:
2. Respuesta a las Métricas:

AL seleccionar el botón de la parte1 se aparece una vista que nos da la posibilidad de subir los ficheros csv: 'jobs', 'departments','hired_employees'
![3](https://github.com/yadelisgv/Globant-Challenge-Flask-Python-SQLITE/assets/40398052/f8d86bc6-3ec3-4190-9e84-33dd0f93e5d3)

Tenemos diferentes respuestas para diversas situaciones:

1. Si se hace clic en el botón "Upload" pero no se ha seleccionado ningún archivo para subir, se mostrará el mensaje "No file provided in the request".
![6](https://github.com/yadelisgv/Globant-Challenge-Flask-Python-SQLITE/assets/40398052/574f9add-1859-4b6f-baa3-6aae2647e243)

2. Si se selecciona un archivo incorrecto, se mostrará el mensaje "Invalid table name provided".
![7](https://github.com/yadelisgv/Globant-Challenge-Flask-Python-SQLITE/assets/40398052/ab09323f-3311-48f5-ace0-b241fb6520bb)

3. Si se selecciona correctamente el archivo y se logra cargar en la base de datos, se mostrará el mensaje "Data uploaded to <nombre_de_la_tabla> successfully".
![5](https://github.com/yadelisgv/Globant-Challenge-Flask-Python-SQLITE/assets/40398052/bc35f5cd-496e-4dc6-a323-e12c0bd3b3ce)

Luego de cargada la data se puede retornar a la página de inicio y seleccionar la parte2 del desafío que nos llevará a la siguiente vista:
![8](https://github.com/yadelisgv/Globant-Challenge-Flask-Python-SQLITE/assets/40398052/3c52f2cf-6a84-4a3b-af19-e278d3caf44e)

En esta parte se muestra lo que se requiere en cada métrica y al elegir en los botones: Requirements1 o Requirements2 podremos ver los resultados impresos en forma de tabla en la misma vista.
![9](https://github.com/yadelisgv/Globant-Challenge-Flask-Python-SQLITE/assets/40398052/6d76a974-9721-41f2-9fda-b0f5cd8bd0b2)
![10](https://github.com/yadelisgv/Globant-Challenge-Flask-Python-SQLITE/assets/40398052/e04a9293-6705-4c5c-a657-0a75ead06c42)


