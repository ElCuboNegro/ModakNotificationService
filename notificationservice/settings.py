# we are calling notificationservice.settings.database_connection_url.get_secret_value(),
# and otificationservice.settings.database_echo,

class Settings:
    def __init__(self):
        self.DATABASE_URL = 'your_database_url'

# Para usarlo, simplemente crea una instancia de Settings
settings = Settings()
print(settings.DATABASE_URL)
