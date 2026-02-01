import os
from django.core.asgi import get_asgi_application
#CA
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'underground_project.settings')
application = get_asgi_application()
