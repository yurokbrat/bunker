from rest_framework.viewsets import ReadOnlyModelViewSet

from bunker_game.game.models.action_card import ActionCard
from bunker_game.game.serializers import ActionCardRetrieveSerializer
from bunker_game.game.serializers.action_card_serializers import (
    ActionCardListSerializer,
)
from bunker_game.utils.mixins import SerializerByActionMixin


class ActionCardViewSet(SerializerByActionMixin, ReadOnlyModelViewSet):
    queryset = ActionCard.objects.all()
    serializer_class = ActionCardRetrieveSerializer
    serializer_action_classes = {
        "retrieve": ActionCardRetrieveSerializer,
        "list": ActionCardListSerializer,
    }
    lookup_field = "uuid"
