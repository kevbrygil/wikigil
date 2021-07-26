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

## Modelos

### Shelf: Una unidad de muebles del edificio. Los productos se encuentran en un estante.

|Propiedad | Tipo esperado | Descripción |
| --- | --- | --- |
| buildingId | FK: Buildind | El edificio en el que se encuentra el estante. |
| productId | FK: Product | El producto que se encuentra actualmente en la estantería |
| employeeId | FK: Employee | El personal que instaló el estante
| name | String | Nombre del estante |
| maxCapacity | Integer | La cantidad máxima de artículos que puede contener el estante |
| availablesItems | Integer | La cantidad de artículos del producto que se encuentran actualmente en el estante |
| latitude | String | Latitud del estante |
| longitude | String | Longitud del estante |


### Muestra en WEB

<img src="https://github.com/kevbrygil/wikigil/blob/main/testweb.png" />