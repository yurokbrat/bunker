import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.exceptions import ObjectDoesNotExist

from bunker_game.game.models import Game, Personage


class GameConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)
        self.game_name: str | None = None
        self.game: Game | None = None
        self.personage: Personage | None = None
        self.personage_uuid: str | None = None
        self.game_uuid: str | None = None

    async def connect(self) -> None:
        self.game_uuid = self.scope["url_route"]["kwargs"]["game_uuid"]
        self.personage_uuid = self.scope["url_route"]["kwargs"].get("personage_id")
        try:
            self.game = await Game.objects.aget(uuid=self.game_uuid)
            if self.personage_uuid:
                self.personage = await Personage.objects.aget(uuid=self.personage_uuid)
            self.game_name = f"game_{self.game_uuid}"
            await self.channel_layer.group_add(self.game_name, self.channel_name)
            await self.accept()
        except ObjectDoesNotExist:
            await self.close()
            return

    async def show_characteristic(self, event: dict) -> None:
        action_type = event.get("type")
        personage_id = event.get("personage_id")
        type_characteristic = event.get("type_characteristic")
        value_characteristic = event.get("value_characteristic")
        is_hidden = event.get("is_hidden")

        await self.send(
            text_data=json.dumps(
                {
                    "type": action_type,
                    "personage_id": personage_id,
                    "type_characteristic": type_characteristic,
                    "value_characteristic": value_characteristic,
                    "is_hidden": is_hidden,
                },
                ensure_ascii=False,
            ),
        )

    async def join_game(self, event: dict) -> None:
        action_type = event.get("type")
        personage_data = event["personage_data"]

        await self.send(
            text_data=json.dumps(
                {
                    "type": action_type,
                    "personage": personage_data,
                },
                ensure_ascii=False,
            ),
        )

    async def exit_game(self, event: dict) -> None:
        action_type = event.get("type")
        personage_data = event["personage_data"]

        await self.send(
            text_data=json.dumps(
                {
                    "type": action_type,
                    "personage": personage_data,
                },
                ensure_ascii=False,
            ),
        )
        await self.channel_layer.group_discard(self.game_name, self.channel_name)

    async def kick_personage(self, event: dict) -> None:
        action_type = event.get("type")
        personage_data = event["personage_data"]

        await self.send(
            text_data=json.dumps(
                {
                    "type": action_type,
                    "personage": personage_data,
                },
                ensure_ascii=False,
            ),
        )

    async def start_game(self, event: dict) -> None:
        action_type = event.get("type")
        game_data = event.get("game_data")

        await self.send(
            text_data=json.dumps(
                {"type": action_type, "game": game_data},
                ensure_ascii=False,
            ),
        )

    async def stop_game(self, event: dict) -> None:
        action_type = event.get("type")
        game_data = event.get("game_data")

        await self.send(
            text_data=json.dumps(
                {"type": action_type, "game": game_data},
                ensure_ascii=False,
            ),
        )

    async def regenerate_game(self, event: dict) -> None:
        action_type = event.get("type")
        new_characteristic_data = event.get("new_characteristic_data")

        await self.send(
            text_data=json.dumps(
                {
                    "type": action_type,
                    "new_characteristic": new_characteristic_data,
                },
                ensure_ascii=False,
            ),
        )

    async def use_action_card(self, event: dict) -> None:
        action_type = event.get("type")
        action_card_data = event.get("action_card_data")

        await self.send(
            text_data=json.dumps(
                {"type": action_type, "action_card": action_card_data},
                ensure_ascii=False,
            ),
        )

    async def start_voting(self, event: dict) -> None:
        action_type = event.get("type")
        voting_data = event.get("voting_data")

        await self.send(
            text_data=json.dumps(
                {"type": action_type, "voting": voting_data},
                ensure_ascii=False,
            ),
        )

    async def send_vote(self, event: dict) -> None:
        action_type = event.get("type")
        vote_data = event.get("vote_data")

        await self.send(
            text_data=json.dumps(
                {"type": action_type, "vote": vote_data},
                ensure_ascii=False,
            ),
        )

    async def stop_voting(self, event: dict) -> None:
        action_type = event.get("type")
        results_data = event.get("results_data")

        await self.send(
            text_data=json.dumps(
                {"type": action_type, "results": results_data},
                ensure_ascii=False,
            ),
        )
