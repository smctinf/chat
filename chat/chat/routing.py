#This file will route to the consumer

from django.urls import path

from . import consumers

websocket_urlspatters = [
    #I will came back to undestand this part of code
    path("ws/chat/<room_name>", consumers.ChatConsumer.as_asgi())
]
