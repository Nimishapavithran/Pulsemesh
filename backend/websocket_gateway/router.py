from django.urls import re_path
from .room_consumers import RoomConsumer

from .consumers import NotificationConsumer


websocket_urlpatterns = [

    re_path(
        r"ws/notifications/$",
        NotificationConsumer.as_asgi(),
    ),

    re_path(
        r"ws/rooms/(?P<room_id>[0-9a-f-]+)/$",
        RoomConsumer.as_asgi(),
    ),
]
