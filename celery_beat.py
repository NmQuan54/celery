from celery.schedules import crontab
from tasks import celery

celery.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
    'multiply-every-minute': {
        'task': 'tasks.multiply',
        'schedule': crontab(minute='*/1'),
        'args': (4, 5)
    },
    'subtract-every-hour': {
        'task': 'tasks.subtract',
        'schedule': crontab(minute=0, hour='*/1'),
        'args': (10, 5)
    },
    'divide-every-day': {
        'task': 'tasks.divide',
        'schedule': crontab(minute=0, hour=0),
        'args': (20, 4)
    },
    'send-bulk-emails-every-day': {
        'task': 'tasks.send_bulk_emails',
        'schedule': crontab(minute=0, hour=0),  # Adjust the schedule as needed
        'args': (['email1@example.com', 'email2@example.com'], 'Subject', 'Message content')
    },
}