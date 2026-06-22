from django.urls import path
from .views import (
    RoomListCreateView,
    RoomDetailView,
)
from .views import (
    RoomListCreateView,
    RoomDetailView,
)
path(
    "rooms/",
    RoomListCreateView.as_view(),
    name="room-list-create",
),

path(
    "rooms/<uuid:pk>/",
    RoomDetailView.as_view(),
    name="room-detail",
),
path(
    "rooms/",
    RoomListCreateView.as_view(),
    name="room-list-create",
),

path(
    "rooms/<uuid:pk>/",
    RoomDetailView.as_view(),
    name="room-detail",
),