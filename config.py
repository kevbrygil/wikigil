class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://aiyqnoic:7jfdAb3WNfj2sgJe0h6SWaZE4tFLrUSs@queenie.db.elephantsql.com:5432/aiyqnoic'

class TestingConfig(Config):
    TESTING = True