from django.urls import path

from bunker_game.consumers import PersonageConsumer

websocket_urlpatterns = [
    path("ws/game/<int:game_uuid>/", PersonageConsumer.as_asgi()),
]
