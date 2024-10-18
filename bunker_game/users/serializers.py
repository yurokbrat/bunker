from rest_framework import serializers

from bunker_game.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "name",
            "url",
            "avatar",
            "date_joined",
            "last_login",
            "last_online",
        )

        extra_kwargs = {
            "url": {"view_name": "users:user-detail", "lookup_field": "username"},
        }
