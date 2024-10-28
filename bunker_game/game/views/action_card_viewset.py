from rest_framework import mixins, viewsets

from bunker_game.game.models.action_card import ActionCard
from bunker_game.game.serializers import ActionCardSerializer


class ActionCardViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ActionCard.objects.all()
    serializer_class = ActionCardSerializer
    lookup_field = "uuid"
