from .models import Room
from .serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class RoomListCreateView(

    generics.ListCreateAPIView
):

    serializer_class = RoomSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Room.objects.all()

    def perform_create(
        self,
        serializer
    ):

        room = serializer.save(
            created_by=self.request.user
        )

        room.members.add(
            self.request.user
        )


class RoomDetailView(

    generics.RetrieveAPIView
):

    serializer_class = RoomSerializer

    permission_classes = [
        IsAuthenticated
    ]

    queryset = Room.objects.all()