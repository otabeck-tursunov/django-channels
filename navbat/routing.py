from django.urls import path
from .consumers import PersonConsumer

websocket_urlpatterns = [
    path('persons/', PersonConsumer.as_asgi()),
]
