from __future__ import absolute_import

import os

from celery import Celery

# from __future__ import absolute_import
# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upscbasicfunda.settings')

app = Celery('upscbasicfunda')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule={
    'every-1-minute':{
        'task':'quiz.tasks.auto_sumbit_task',
        'schedule':60,
    }
}
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')