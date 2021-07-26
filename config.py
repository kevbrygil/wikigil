class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://nnuxljcw:g9LFwxO9dsMN5SpdKTyEsVOC53G77nTO@chunee.db.elephantsql.com/nnuxljcw'

class TestingConfig(Config):
    TESTING = True
