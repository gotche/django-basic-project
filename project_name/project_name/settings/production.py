from configurations import Configuration, values

from .base import BaseSettings


class {{ project_name }}Settings(BaseSettings, Configuration):
    DEBUG = False
    DATABASE_URL = values.DatabaseURLValue()
