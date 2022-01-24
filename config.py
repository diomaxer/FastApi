from os import environ


class DatabaseConfig(object):
    DB_NAME = environ.get("DB_NAME", "fast_api_test")
    DB_PASSWORD = environ.get("DB_PASSWORD", "password")
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_PORT = environ.get("DB_PORT", "5432")
    DB_USER = environ.get("DB_USER", "caltatnew")

    DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
