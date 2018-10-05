import os

SESSION_COOKIE_NAME = 'session'
SESSION_COOKIE_PATH = '/'
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = False
UPLOAD_DIR = 'static/upload'

SENTRY_DSN = os.environ.get("SENTRY_DSN")

{% if cookiecutter.use_celery == 'y' %}
CELERY_RESULT_BACKEND = 'redis://'
RABBITMQ_DEFAULT_USER = os.environ.get("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.environ.get("RABBITMQ_DEFAULT_PASS")
RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST")
RABBITMQ_PORT = os.environ.get("RABBITMQ_PORT")
BROKER_URL = f'pyamqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}//'
{% endif %}

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB", '{{cookiecutter.app_name}}')
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", '{{cookiecutter.app_name}}_db')
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", '5432')
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

SERVER_NAME = os.environ.get("SERVER_NAME")
SECRET_KEY = os.environ.get("SECRET_KEY")

SCHEME = os.environ.get('SCHEME', 'http')
DOMAIN = os.environ.get('DOMAIN', '127.0.0.1')
PORT = os.environ.get('PORT', 5000)

{% if cookiecutter.use_mail == 'y' %}
MAIL_SERVER = os.environ.get("MAIL_SERVER")
MAIL_PORT = os.environ.get("MAIL_PORT")
MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL")
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_DEBUG = os.environ.get("MAIL_DEBUG")
{% endif %}

