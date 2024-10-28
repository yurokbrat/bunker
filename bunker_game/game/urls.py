from django.urls import URLPattern, URLResolver, include, path
from rest_framework_nested.routers import SimpleRouter

from bunker_game.game.views import (
    ActionCardViewSet,
    BunkerViewSet,
    CatastropheViewSet,
    GameViewSet,
    PersonageViewSet,
)

router = SimpleRouter()

router.register("games", GameViewSet, basename="games")
router.register("bunkers", BunkerViewSet)
router.register("catastrophes", CatastropheViewSet)
router.register("action-cards", ActionCardViewSet, basename="action-cards")
router.register("personages", PersonageViewSet, basename="personages")

app_name = "game"
urlpatterns: list[URLPattern | URLResolver] = [
    path("", include(router.urls)),
]
