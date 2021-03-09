release: python manage.py migrate --noinput
web: gunicorn upscbasicfunda.wsgi
worker: REMAP_SIGTERM=SIGQUIT celery -A upscbasicfunda worker -l info