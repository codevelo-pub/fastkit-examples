import os

CONNECTIONS = {
    'default': {
        'driver': os.getenv('DB_DRIVER', 'sqlite'),
        'database': os.getenv('DB_NAME', 'quickstart.db'),
        'echo': False  # Set to True to see SQL queries
    }
}