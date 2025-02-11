from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend='redis://redis:6379/0',  # Redis làm backend
        broker='redis://redis:6379/0'   # Redis làm message broker
    )
    celery.conf.update(app.config)
    return celery
