"""
WSGI config for fibonacci project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fibonacci.settings')

application = get_wsgi_application()
