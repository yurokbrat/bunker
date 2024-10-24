from django.urls.conf import include, path

from bunker_game.game.views.build_info_view import BuildInfoView

urlpatterns = [
    path("build-info/", BuildInfoView.as_view(), name="build-info"),
    path("", include("bunker_game.game.urls")),
    path("", include("bunker_game.users.urls")),
]
