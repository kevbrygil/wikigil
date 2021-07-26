class Config(object):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'postgresql://nnuxljcw:g9LFwxO9dsMN5SpdKTyEsVOC53G77nTO@chunee.db.elephantsql.com/nnuxljcw'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://nnuxljcw:g9LFwxO9dsMN5SpdKTyEsVOC53G77nTO@chunee.db.elephantsql.com/nnuxljcw'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
