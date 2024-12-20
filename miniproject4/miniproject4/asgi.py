# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Mini Project 4

"""
ASGI config for miniproject4 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproject4.settings')

application = get_asgi_application()
