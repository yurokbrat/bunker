import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.exceptions import ObjectDoesNotExist

from bunker_game.game.models import Personage


class PersonageConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)
        self.game: str | None = None
        self.game_name: str | None = None
        self.room: str | None = None
        self.personage: Personage | None = None
        self.personage_id: int | None = None
        self.game_uuid: str | None = None

    async def connect(self) -> None:
        self.game_uuid = self.scope["url_route"]["kwargs"]["game_uuid"]
        try:
            self.personage = await Personage.objects.aget(games=self.game_uuid)
            self.personage_id = self.personage.id
        except ObjectDoesNotExist:
            await self.close()
            return

        self.game_name = f"game_{self.game_uuid}"

        await self.channel_layer.group_add(self.game_name, self.channel_name)

        await self.accept()

    async def receive(self, text_data: str) -> None:
        await self.channel_layer.group_send(
            self.game_name,
            {
                "type": "update_characteristics",
                "personage_id": self.personage_id,
            },
        )

    async def update_characteristics(self, event: dict) -> None:
        personage_id = event["personage_id"]
        characteristic_type = event.get("characteristic_type")
        is_hidden = event.get("is_hidden")

        await self.send(
            text_data=json.dumps(
                {
                    "personage_id": personage_id,
                    "characteristic_type": characteristic_type,
                    "is_hidden": is_hidden,
                },
            ),
        )

    async def disconnect(self, close_code: int) -> None:
        await self.channel_layer.group_discard(self.game_name, self.channel_name)
