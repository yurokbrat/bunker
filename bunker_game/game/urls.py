from django.urls import URLPattern, URLResolver, include, path
from rest_framework.routers import SimpleRouter

from bunker_game.game.views import BunkerViewSet, CatastropheViewSet, PersonageViewSet

router = SimpleRouter()

router.register("personages", PersonageViewSet)
router.register("bunkers", BunkerViewSet)
router.register("catastrophes", CatastropheViewSet)


app_name = "game"
urlpatterns: list[URLPattern | URLResolver] = [
    path("", include(router.urls)),
]
