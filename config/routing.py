from django.urls import path

from bunker_game.consumers import GameConsumer

websocket_urlpatterns = [
    path("ws/game/<str:game_uuid>/", GameConsumer.as_asgi()),
    path(
        r"^ws/game/(?P<game_uuid>[^/]+)/(?P<personage_id>[^/]+)?/$",
        GameConsumer.as_asgi(),
    ),
]
