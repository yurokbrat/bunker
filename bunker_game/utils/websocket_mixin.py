from typing import Any
from uuid import UUID

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models import Model
from rest_framework.request import Request

from bunker_game.game.models import Personage
from bunker_game.game.serializers.personage_serializers import (
    PersonageActionCardSerializer,
    PersonageShortSerializer,
)


class WebSocketMixin:
    def web_socket_send_characteristic(
        self,
        game_uuid: UUID | Any,
        personage_id: int,
        type_characteristic: str,
        value_characteristic: Any,
    ) -> None:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"game_{game_uuid}",
            {
                "type": "show_characteristic",
                "personage_id": personage_id,
                "type_characteristic": type_characteristic,
                "value_characteristic": value_characteristic,
                "is_hidden": False,
            },
        )

    def web_socket_join_game(
        self,
        game_uuid: str,
        personage: Personage,
        request: Request,
    ) -> None:
        personage_serializer = PersonageShortSerializer(
            personage,
            context={"request": request},
        )
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"game_{game_uuid}",
            {
                "type": "join_game",
                "personage_data": personage_serializer.data,
            },
        )

    def web_socket_exit_game(
        self,
        game_uuid: str,
        personage: Personage,
        request: Request,
    ) -> None:
        personage_serializer = PersonageShortSerializer(
            personage,
            context={"request": request},
        )
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"game_{game_uuid}",
            {
                "type": "exit_game",
                "personage_data": personage_serializer.data,
            },
        )

    def web_socket_start_game(self, game_uuid: UUID, game_data: dict[str, Any]) -> None:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"game_{game_uuid}",
            {
                "type": "start_game",
                "game_data": game_data,
            },
        )

    def web_socket_send_action_card(
        self,
        game_uuid: str,
        action_card: Model,
        request: Request,
    ) -> None:
        action_card_serializer = PersonageActionCardSerializer(
            action_card,
            context={"request": request},
        )
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"game_{game_uuid}",
            {
                "type": "use_action_card",
                "action_card_data": action_card_serializer.data,
            },
        )
