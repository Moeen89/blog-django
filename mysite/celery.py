# celery.py
from celery import Celery
from celery.schedules import crontab

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'my-periodic-task': {
        'task': 'snippets.tasks.sum_snippets_click',
        'schedule': 10,
    },
}
