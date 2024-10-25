from typing import Any

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from bunker_game.game.models import Bunker
from bunker_game.game.serializers import BunkerRoomsSerializer, BunkerSerializer


class BunkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bunker.objects.filter(is_generated=False)
    serializer_class = BunkerSerializer
    lookup_field = "uuid"

    @action(detail=True, methods=("GET",), serializer_class=BunkerRoomsSerializer)
    def rooms(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        bunker: Bunker = self.get_object()
        serializer = BunkerRoomsSerializer(
            instance=bunker.rooms,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
