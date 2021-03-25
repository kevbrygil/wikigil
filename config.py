class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://eivsdjze:JE1XNgPmmeZBvhf2Aae-wKHxHuwx0620@queenie.db.elephantsql.com:5432/eivsdjze'

class TestingConfig(Config):
    TESTING = True