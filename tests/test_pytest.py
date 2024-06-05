import pytest

# Import specific modules for testing
from notificationservice.notifications.notifications import module as notifications_module
from notificationservice.api.api import module as api_module
from notificationservice.config.config import module as config_module
from notificationservice.rate_limiter.rate_limiter import module as rate_limiter_module

# Test access to the notifications function
def test_notifications_access():
    result = notifications_module()
    assert result == "Hello from notifications"

# Test access to the api function
def test_api_access():
    result = api_module()
    assert result == "Hello from api"

# Test access to the config function
def test_config_access():
    result = config_module()
    assert result == "Hello from config"

# Test access to the rate_limiter function
def test_rate_limiter_access():
    result = rate_limiter_module()
    assert result == "Hello from rate_limiter"
