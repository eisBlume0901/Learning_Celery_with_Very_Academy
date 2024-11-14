# Have to add celery to __init__.py to make it work with Django so that
# everytime Django starts, it will also start the celery worker

from .celery import app as celery_app # Importing the celery from the celery.py file

__all__ = ('celery_app',)
