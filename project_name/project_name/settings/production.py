from configurations import Configuration, values

from .base import BaseSettings


class Production(BaseSettings, Configuration):
    DEBUG = False
    DATABASE_URL = values.DatabaseURLValue()
