from uwsgiconf.config import configure_usgi
from uwsgi.presets.nice import PythonSection
def get_config():
    section = PythonSection.bootstrap('http://127.0.0.1:8000',wsgi_module='wsgi')
    return section

configure_usgi(get_config)