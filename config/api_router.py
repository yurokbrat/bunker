from django.urls.conf import path, include

urlpatterns = [
    path("", include("bunker_game.game.urls")),
    path("", include("bunker_game.users.urls")),
    path("", include("bunker_game.room.urls")),

]
