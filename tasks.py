from celery import Celery

celery = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task
def add(x, y):
    return x + y

@celery.task
def multiply(x, y):
    return x * y

@celery.task
def subtract(x, y):
    return x - y

@celery.task
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

@celery.task
def send_email(to_email, subject, message):
    # Implement email sending logic here
    return f"Email sent to {to_email} with subject {subject}"

@celery.task
def send_bulk_emails(email_list, subject, message):
    results = []
    for email in email_list:
        result = send_email(email, subject, message)
        results.append(result)
    return results