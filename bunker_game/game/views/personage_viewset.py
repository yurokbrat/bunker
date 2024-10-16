from rest_framework import viewsets

from bunker_game.game.models import Personage
from bunker_game.game.serializers import PersonageSerializer


class PersonageViewSet(viewsets.ModelViewSet):
    queryset = Personage.objects.all()
    serializer_class = PersonageSerializer

