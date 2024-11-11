"""
WSGI config for Learning_Celery_with_Very_Academy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learning_Celery_with_Very_Academy.settings')

application = get_wsgi_application()
