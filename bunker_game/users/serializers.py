from rest_framework import serializers

from bunker_game.users.models import User


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields: tuple[str, ...] = (
            "uuid",
            "username",
            "name",
            "url",
            "avatar",
        )
        extra_kwargs = {
            "url": {"view_name": "users:user-detail", "lookup_field": "uuid"},
            "avatar": {"read_only": True},
        }


class UserSerializer(UserShortSerializer):
    class Meta(UserShortSerializer.Meta):
        fields = (
            *UserShortSerializer.Meta.fields,
            "date_joined",
            "last_login",
            "last_online",
        )

        extra_kwargs = {
            **UserShortSerializer.Meta.extra_kwargs,
            "date_joined": {"read_only": True},
            "last_login": {"read_only": True},
            "last_online": {"read_only": True},
        }
