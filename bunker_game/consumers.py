import json

from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist


class PersonageConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.game = None
        self.game_name = None
        self.room = None
        self.personage = None
        self.personage_id = None
        self.game_uuid = None

    async def connect(self):
        self.game_uuid = self.scope["url_route"]["kwargs"]["game_uuid"]
        try:
            Personage = apps.get_model("game", "Personage")
            self.personage = await Personage.objects.aget(games=self.game_uuid)
            self.personage_id = self.personage.id
        except ObjectDoesNotExist:
            await DenyConnection(f"Game for personage {self.personage_id} not found")

        self.game_name = f"game_{self.game_uuid}"

        await self.channel_layer.group_add(self.game_name, self.channel_name)

        await self.accept()

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.game_name,
            {
                "type": "update_characteristics",
                "personage_id": self.personage_id,
            },
        )

    async def update_characteristics(self, event):
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

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.game_name, self.channel_name)
