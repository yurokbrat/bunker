from django.urls import URLPattern, URLResolver, include, path
from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter

from bunker_game.game.views import (
    ActionCardViewSet,
    BunkerViewSet,
    CatastropheViewSet,
    GameViewSet,
    PersonageViewSet,
)
from bunker_game.game.views.vote_viewset import VoteViewSet

router = SimpleRouter()

router.register("games", GameViewSet, basename="games")
router.register("bunkers", BunkerViewSet)
router.register("catastrophes", CatastropheViewSet)
router.register("action-cards", ActionCardViewSet, basename="action-cards")
router.register("personages", PersonageViewSet, basename="personages")

vote_router = NestedSimpleRouter(router, parent_prefix="games", lookup="game")
vote_router.register("voting", VoteViewSet, basename="votes")

app_name = "game"
urlpatterns: list[URLPattern | URLResolver] = [
    path("", include(router.urls)),
    path("", include(vote_router.urls)),
]
