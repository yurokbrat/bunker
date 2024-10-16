from rest_framework import viewsets

from bunker_game.room.models import Room
from bunker_game.room.serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.filter(users__isnull=False).order_by("id")
    serializer_class = RoomSerializer
