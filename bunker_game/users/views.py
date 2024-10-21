from django.db import models
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from bunker_game.users.models import User
from bunker_game.users.serializers import UserSerializer


class UserViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("last_online")

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def free(self, request):
        free_users = User.objects.filter(
            models.Q(personage__game__is_active=False),
        )
        serializer = UserSerializer(free_users, context={"request": request}, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def gaming(self, request):
        gaming_users = User.objects.filter(personage__game__is_active=True)

        serializer = UserSerializer(
            gaming_users,
            context={"request": request},
            many=True,
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def creators(self, request):
        creator_users = User.objects.filter(game_creator__isnull=False)

        serializer = UserSerializer(
            creator_users,
            context={"request": request},
            many=True,
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)
