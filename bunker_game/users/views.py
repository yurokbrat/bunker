from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from bunker_game.users.models import User
from bunker_game.users.serializers import UserSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("last_online")
    lookup_field = "username"

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def free(self, request):
        gaming_users = User.objects.filter(room__isnull=True)
        serializer = UserSerializer(
            gaming_users,
            context={"request": request},
            many=True,
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False)
    def gaming(self, request):
        gaming_users = User.objects.filter(room__isnull=False)
        serializer = UserSerializer(
            gaming_users,
            context={"request": request},
            many=True,
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)
