from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from bunker_game.game.models.action_card import ActionCard
from bunker_game.game.serializers.action_card_serializers import ActionCardSerializer


class ActionCardViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ActionCard.objects.all()
    serializer_class = ActionCardSerializer
    lookup_field = "uuid"

    @action(detail=False, methods=("GET",))
    def random(self, request, *args, **kwargs):
        action_card = ActionCard.objects.order_by("?").first()
        serializer = ActionCardSerializer(
            instance=action_card,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
