from rest_framework.viewsets import ReadOnlyModelViewSet

from bunker_game.game.models import Bunker
from bunker_game.game.serializers import BunkerRetrieveSerializer
from bunker_game.game.serializers.bunker_serializers import BunkerListSerializer
from bunker_game.utils.mixins import SerializerByActionMixin


class BunkerViewSet(SerializerByActionMixin, ReadOnlyModelViewSet):
    queryset = Bunker.objects.filter(is_generated=False)
    serializer_class = BunkerListSerializer
    serializer_action_classes = {
        "list": BunkerListSerializer,
        "retrieve": BunkerRetrieveSerializer,
    }
    lookup_field = "uuid"
