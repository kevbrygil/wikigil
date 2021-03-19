from flask_migrate import Migrate, MigrateCommand
from config import SQLALCHEMY_DATABASE_URI
from app.database import db
from flask import Flask
from flask_script import Manager
from app import create_app
 
app = create_app('config')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
  
if __name__ == '__main__':
    manager.run()