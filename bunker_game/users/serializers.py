from rest_framework import serializers

from bunker_game.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = (
            "uuid",
            "username",
            "name",
            "url",
            "avatar",
            "date_joined",
            "last_login",
            "last_online",
        )

        extra_kwargs = {
            "url": {"view_name": "users:user-detail", "lookup_field": "uuid"},
            "avatar": {"read_only": True},
            "date_joined": {"read_only": True},
            "last_login": {"read_only": True},
            "last_online": {"read_only": True},
        }
