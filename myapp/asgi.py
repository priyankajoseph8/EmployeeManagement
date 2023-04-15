"""
ASGI config for myapp project.

It exposes the ASGI callable as a module-level variable named ``ASGI_APPLICATION``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

ASGI_APPLICATION = get_wsgi_application()
