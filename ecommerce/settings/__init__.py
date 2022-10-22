import os
import importlib

ENV = os.getenv('ENV', 'development')

env_settings = importlib.import_module(f'ecommerce.settings.{ENV}')

globals().update(vars(env_settings))

try:
    from .base import *
except ImportError:
    pass