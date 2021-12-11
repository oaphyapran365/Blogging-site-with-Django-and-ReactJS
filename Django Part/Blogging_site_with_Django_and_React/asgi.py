"""
ASGI config for Blogging_site_with_Django_and_React project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blogging_site_with_Django_and_React.settings')

application = get_asgi_application()
