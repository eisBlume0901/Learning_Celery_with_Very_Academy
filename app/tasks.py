
from celery import shared_task

@shared_task # This decorator is used to create a task and way for celery to recognize it
def add(x, y):
    return x + y