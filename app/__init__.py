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
    
    from app.controllers.store import store
    app.register_blueprint(store, url_prefix='/api/stores')

    from app.controllers.product import product
    app.register_blueprint(product, url_prefix='/api/products')
    
    from app.controllers.inventory import inventory
    app.register_blueprint(inventory, url_prefix='/api/inventoryitems')

    return app