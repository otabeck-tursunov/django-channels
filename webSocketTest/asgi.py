import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webSocketTest.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

django_asgi_application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
import navbat.routing

application = ProtocolTypeRouter({
    "http": django_asgi_application,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            navbat.routing.websocket_urlpatterns
        )
    )
})