# Aplicación Flask

Desarrollo web perteneciente al segmento backend con Python del curso dado en el 2024 correspondiente a Codo a Codo - Full stack Python.

## Ejecución del proyecto

Considerando que se tiene instalado Python en el equipo, ademas de una servidor de bases de datos SQL corriendo localmente, realizar los siguientes pasos ubicados dentro de la carpeta donde se clono este proyecto:

Paso 1) Descargar y crear un espacio virtual
```bash
$   pip install virtualenv
$   python -m venv env
```

Paso 2) Activar el espacio virtual
```bash
$   . \env/Scripts/activate
```

Paso 3) Instalar todos los modulos necesarios del proyecto
```bash
$   pip install -r requirements.txt
```

Paso 4) Crear en la raiz de la carpeta del proyecto un archivo llamado `.env` y dentro agregar lo siguiente con los datos correspondientes de cada usuario:
```bash
    MYSQL_USER = 'usuario de la base de datos' //Generalmente 'root'
    MYSQL_PASSWORD = 'constraseña'  //Generalmente 'root'
    MYSQL_HOST = 'host donde se encuentra levantado el proyecto' //Generalmente 'localhost'
    MYSQL_DATABASE = 'Nombre de la base de datos a utilizar'
```

Paso 5) Levantar el proyecto Flask localmente
```bash
$   python run.py
```
Si todo se realizo correctamente, este ultimo paso iniciara la aplicación Flask para utilizar. Considerar que este comando tan solo inicia la aplicacíon teniendo completamente la base de datos vacia.
Para poder iniciar la aplicación con datos ya cargados o restaurar la base de datos con datos predeterminados, iniciar la aplicación de la siguiente manera:
```bash
$   python run.py load_data
```
## Vistas que ofrece la app

* `/`: Pagina inicial de la app.
* `/location`: Pagina inicial de las ubicaciones.
* `/movies`: Pagina inicial de las peliculas.
  
## Endpoint que ofrece la api para respuestas en formato JSON

* `/api/locations`: Lista de ubicaciones.

