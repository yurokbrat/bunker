from typing import Any

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from bunker_game.users.filters import UserFilter
from bunker_game.users.models import User
from bunker_game.users.serializers import UserListSerializer, UserSerializer
from bunker_game.utils.mixins import SerializerByActionMixin


class UserViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    SerializerByActionMixin,
    GenericViewSet,
):
    serializer_class = UserSerializer
    serializer_action_classes = {
        "list": UserListSerializer,
        "retrieve": UserSerializer,
    }
    queryset = User.objects.all().order_by("last_online")
    lookup_field = "uuid"
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter

    @action(detail=False)
    def me(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
