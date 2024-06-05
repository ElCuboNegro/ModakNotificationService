import sys
import os
import pytest

# Agregar src al PYTHONPATH
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)

# Importar módulos específicos para las pruebas
from notifications.notifications import module as notifications_module
from api.api import module as api_module
from config.config import module as config_module
from rate_limiter.rate_limiter import module as rate_limiter_module


# Prueba de acceso a la función de notifications
def test_notifications_access():
    result = notifications_module()
    assert result == "Hello from notifications"


# Prueba de acceso a la función de api
def test_api_access():
    result = api_module()
    assert result == "Hello from api"


# Prueba de acceso a la función de config
def test_config_access():
    result = config_module()
    assert result == "Hello from config"


# Prueba de acceso a la función de rate_limiter
def test_rate_limiter_access():
    result = rate_limiter_module()
    assert result == "Hello from rate_limiter"
