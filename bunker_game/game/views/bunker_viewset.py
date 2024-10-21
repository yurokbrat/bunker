from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from bunker_game.game.models import Bunker
from bunker_game.game.serializers import BunkerSerializer
from bunker_game.game.serializers.bunker_serializers import BunkerRoomsSerializer


class BunkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bunker.objects.all()
    serializer_class = BunkerSerializer
    lookup_field = "uuid"

    @action(detail=True, methods=("GET",), serializer_class=BunkerRoomsSerializer)
    def rooms(self, request, *args, **kwargs):
        bunker: Bunker = self.get_object()
        serializer = BunkerRoomsSerializer(
            instance=bunker.rooms,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
