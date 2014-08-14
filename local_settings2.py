
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "428fbae2-0f87-4f9b-9e10-3f6ea108790bac356a05-2af8-4c2a-b12e-658e2a8c03a80bc7fb54-562b-4cbb-9d34-0625477973c5"
NEVERCACHE_KEY = "7933a1d2-6f3f-41f1-a8c9-30e1f08a33ecff784839-7d29-4f6a-994f-9b1a67d967b1beff154f-d3ce-472d-a678-c112c80b0175"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "postgres",
        # Not used with sqlite3.
        "USER": "postgres",
        # Not used with sqlite3.
        "PASSWORD": "dbpostgres",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "5432",
    }
}

