from rest_framework import viewsets

from bunker_game.game.models import Bunker
from bunker_game.game.serializers import BunkerSerializer


class BunkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bunker.objects.all()
    serializer_class = BunkerSerializer
