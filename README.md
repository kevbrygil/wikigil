# Reto Cargamos

### Sistema de gestión de existencias

**Framework for API Rest**:

```
Se decidió usar el framework flask de Python, que es un micro-framework que nos permite 
crear aplicaciones de manera rapida y con un mínimo número de codigo.
```

### Librerias y Frameworks

**Flask-SQLAlchemy**: Por el tiempo corto, un ORM puede ayudar para la comunicación con la bd, Usando Flask-SQLAlchemy definimos las tablas, columnas y es totalmente funcional para uso en aplicaciones básicas y se extiende fácilmente para aplicaciones grandes.

**Flask-Restful/Flask-RestPlus**: Nos permite crear una API REST donde incluye las funciones basicas CRUD(Create, Read and Delete)

**unittest**: Para la realización de pruebas unitarias, unittest esta inspirado en JUnit, admite la automatización de pruebas y el cierre para las dichas pruebas.

### Herramientas necesarias
- Python 3.8.5
- Para nuestra creación de nuestro environment: Pip y Pipenv

### Instalación

Usando la herramienta de Pipenv instalada, solamente requerimos sincronizar
nuestro entorno de desarrollo y luego la activamos:

```
$ pipenv sync
$ pipenv shell
```

La configuracion de la base de datos, migraciones, environment y arranque de la aplicación lo podemos verificar
en los archivos:

- config.py
- run.py
- migrate.py

Se tiene configurado una base de datos de prueba, por lo cual, no es necesario aplicar migraciones, podemos 
arrancar la aplicación con solo realizar lo siguiente:

```
$ pipenv sync
$ pipenv shell
$ python run.py
```

Si desea utilizar una base de datos externa, debe ejecutar los siguientes comandos para la migración de base de datos:

```
$ python migrate.py db init
$ python migrate.py db migrate  
$ python migrate.py db upgrade
```

### Análisis y solución del problema

Por falta de tiempo solo se explicara la parte de existencia del producto:

Se ha creado una entidad Inventory de tabla puente de shelf específicamente para mantener tanto el recuento en el almacen/estante como el recuento en el almacén en una sola entidad. En cualquier cálculo solo estaría involucrada la entidad Inventory. El stock se reduciría y el shelfcount aumentaria.

### Muestra en WEB

https://github.com/kevbrygil/wikigil/blob/main/testweb.png