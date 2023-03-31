import os 

POSTGRES_HOST= os.getenv("PG_DBNAME", "localhost")
POSTGRES_PORT= os.getenv("PG_PORT", "5432")
POSTGRES_USERNAME=os.getenv("PG_USERNAME", "postgres")
POSTGRES_USER_PASSWORD=os.getenv("PG_PASSWORD", "postgres")
POSTGRES_DBNAME=os.getenv("PG_DBNAME", "postgres")

DEBUG= os.getenv("DEBUG_MODE", "false")
AMBIENTE_ATUAL=os.getenv("EXEC_MODE", "dev")

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': POSTGRES_DBNAME,
        'USER': POSTGRES_USERNAME,
        'PASSWORD': POSTGRES_USER_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}
