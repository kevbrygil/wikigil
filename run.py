# TODO: Ejecutar la aplicación usando el servidor web incorporado de Flask
from app import create_app

app = create_app('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=8001)