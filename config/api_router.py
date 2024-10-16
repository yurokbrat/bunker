from django.urls.conf import include, path

urlpatterns = [
    path("", include("bunker_game.game.urls")),
    path("", include("bunker_game.users.urls")),
    path("", include("bunker_game.room.urls")),
]
