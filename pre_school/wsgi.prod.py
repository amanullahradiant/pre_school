"""
WSGI config for pre_school project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pre_school.conf.prod') # lets change the default setting module. from wsgi -> conf.prod.py

application = get_wsgi_application()
