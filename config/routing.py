from django.urls import path, re_path

from bunker_game.consumers import PersonageConsumer

websocket_urlpatterns = [
    path("ws/game/<int:game_id>/", PersonageConsumer.as_asgi()),
]
