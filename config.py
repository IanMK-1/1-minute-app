class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:ian@localhost/pitch'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
