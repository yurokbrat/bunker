from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from bunker_game.game.models import Catastrophe
from bunker_game.game.serializers import CatastropheRetrieveSerializer
from bunker_game.game.serializers.catastrophe_serializers import (
    CatastropheListSerializer,
)
from bunker_game.utils.mixins import SerializerByActionMixin


class CatastropheViewSet(SerializerByActionMixin, ReadOnlyModelViewSet):
    queryset = Catastrophe.objects.all()
    serializer_class = CatastropheRetrieveSerializer
    serializer_action_classes = {
        "list": CatastropheListSerializer,
        "retrieve": CatastropheRetrieveSerializer,
    }
    lookup_field = "uuid"
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("impact_level",)
