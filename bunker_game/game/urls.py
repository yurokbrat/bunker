from django.urls import URLPattern, URLResolver, include, path
from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter


from bunker_game.game.views import BunkerViewSet, CatastropheViewSet, PersonageViewSet
from bunker_game.game.views.game_viewset import GameViewSet

router = SimpleRouter()

router.register("games", GameViewSet, basename="games")
router.register("bunkers", BunkerViewSet)
router.register("catastrophes", CatastropheViewSet)

personage_router = NestedSimpleRouter(router, "games", lookup="game")
personage_router.register("personages", PersonageViewSet, basename="game-personages")


app_name = "game"
urlpatterns: list[URLPattern | URLResolver] = [
    path("", include(router.urls)),
    path("", include(personage_router.urls)),
]
