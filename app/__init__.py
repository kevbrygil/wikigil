from flask import Flask, render_template, send_from_directory
from app.database import db
import os

def create_app(config_filename):
    app = Flask(__name__)

    app.config.from_object(config_filename)

    db.init_app(app)

    @app.route('/<path:filename>')
    def serve_static(filename):
        return send_from_directory(os.path.join('.', 'templates'), filename)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    from app.resources.shelf import shelf
    from app.resources.building import building
    from app.resources.product import product
    from app.resources.employee import employee
    from app.resources.order import order

    app.register_blueprint(shelf, url_prefix='/api/shelves')
    app.register_blueprint(building, url_prefix='/api/buildings')
    app.register_blueprint(product, url_prefix='/api/products')
    app.register_blueprint(employee, url_prefix='/api/employees')
    app.register_blueprint(order, url_prefix='/api/orders')

    return app