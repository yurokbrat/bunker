import django_filters

from bunker_game.users.models import User


class UserFilter(django_filters.FilterSet):
    is_gaming = django_filters.BooleanFilter(
        field_name="personage__game__is_active",
        lookup_expr="exact",
        label="Играют сейчас",
    )
    is_creator_game = django_filters.BooleanFilter(
        field_name="game_creator",
        lookup_expr="isnull",
        exclude=True,
        label="Создатели игр",
    )

    class Meta:
        model = User
        fields = ("is_gaming", "is_creator_game")
