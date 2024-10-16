from rest_framework import viewsets

from bunker_game.game.models import Catastrophe
from bunker_game.game.serializers.catastrophe_serializers import CatastropheSerializer


class CatastropheViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Catastrophe.objects.all()
    serializer_class = CatastropheSerializer
