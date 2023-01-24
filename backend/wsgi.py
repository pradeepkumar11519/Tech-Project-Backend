"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
def application(env,start_response):
    from uwsgiconf.runtime.platform import uesgi
    start_response('200 OK',[('Content-Type','text/html')])
    response = f'{uwsgi.get_version()}:{uwsgi.request.id}'
    return response.encode()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
