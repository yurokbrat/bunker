from rest_framework import viewsets

from bunker_game.game.models import Bunker
from bunker_game.game.serializers import BunkerSerializer


class BunkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bunker.objects.filter(is_generated=False)
    serializer_class = BunkerSerializer
    lookup_field = "uuid"
