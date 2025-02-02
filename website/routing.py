# website/routing.py

from django.urls import re_path, path

from website.views import consumers

websocket_urlpatterns = [
    re_path(r'ws/rooms/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/framework/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
