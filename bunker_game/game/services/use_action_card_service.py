from collections.abc import Collection
from typing import Any
from uuid import UUID

from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from bunker_game.game.constants import (
    ALL_INTERACTIONS_ACTIONS,
    ANOTHER_PERSONAGE_INTERACTIONS_ACTIONS,
    DEFAULT_CHARACTERISTICS,
    GAME_INTERACTIONS_ACTIONS,
    MYSELF_INTERACTIONS_ACTIONS,
)
from bunker_game.game.enums import ActionCardTargetChoice, PhobiaStageChoice
from bunker_game.game.models import (
    CharacteristicVisibility,
    Game,
    Personage,
)
from bunker_game.game.models.action_card_usage import ActionCardUsage
from bunker_game.game.services.create_random_game_characteristics import (
    generate_random_bunker,
    generate_random_catastrophe,
)
from bunker_game.game.services.regenerate_characteristic_service import (
    RegenerateCharacteristicService,
)
from bunker_game.utils.websocket_mixin import WebSocketMixin


class UseActionCardService(WebSocketMixin):
    def __call__(
        self,
        card_key: str,
        personage_instance: Personage,
        game: Game,
        target_uuid: str | None = None,
        showing_characteristic_type: str | None = None,
    ) -> ActionCardUsage:
        action_card_usage = get_object_or_404(ActionCardUsage, card__key=card_key)
        if action_card_usage.is_used:
            message_error = "Эта карта действия уже использовалась."
            raise ValidationError(message_error)
        type_action = card_key.split("_")[0]
        target_type = action_card_usage.card.target
        type_characteristic = card_key.split("_")[1]

        if (
            type_action in GAME_INTERACTIONS_ACTIONS
            and target_type == ActionCardTargetChoice.GAME
        ):
            self.handle_game_interactions(
                type_action,
                type_characteristic,
                game,
                card_key,
            )

        if (
            type_action in MYSELF_INTERACTIONS_ACTIONS
            and target_type == ActionCardTargetChoice.MYSELF
        ):
            self.handle_myself_interactions(
                type_action,
                personage_instance,
                type_characteristic,
                card_key,
            )

        if (
            type_action in ALL_INTERACTIONS_ACTIONS
            and target_type == ActionCardTargetChoice.ALL
        ):
            self.handle_all_interactions(type_characteristic, game, card_key)

        if (
            type_action in ANOTHER_PERSONAGE_INTERACTIONS_ACTIONS
            and target_type == ActionCardTargetChoice.ANOTHER_PERSONAGE
        ):
            another_personage = get_object_or_404(Personage, uuid=target_uuid)
            self.handle_another_personage_interactions(
                type_action,
                personage_instance,
                another_personage,
                type_characteristic,
                card_key,
            )

        action_card_usage.is_used = True
        action_card_usage.save()
        return action_card_usage

    def handle_game_interactions(
        self,
        type_action: str,
        type_characteristic: str,
        game: Game,
        card_key: str,
    ) -> None:
        if type_action == "regenerate":
            regenerate_characteristic_map = {
                "bunker": generate_random_bunker,
                "catastrophe": generate_random_catastrophe,
            }
            regenerate_characteristic_map[type_characteristic]()

        elif type_action == "edit":
            if (card_key.split("_")[4]) == "plus":
                game.num_places += 1
            else:
                game.num_places -= 1
            game.save()

        # Временно, обсудить
        if type_action == "info":
            ...

    def handle_myself_interactions(
        self,
        type_action: str,
        personage_instance: Personage,
        type_characteristic: str,
        card_key: str,
    ) -> None:
        if type_action == "regenerate":
            RegenerateCharacteristicService()(
                personage_instance,
                type_characteristic,
            )
        elif type_action == "fix":
            type_interaction = card_key.split("_")[2]
            num_interaction = int(card_key.split("_")[3])
            if type_characteristic == "age":
                self.update_age(
                    personage_instance,
                    num_interaction,
                    type_interaction,
                )
            elif type_action == "disease":
                if personage_instance.disease:
                    personage_instance.disease.degree_percent -= num_interaction  # type: ignore[operator]

    def handle_all_interactions(
        self,
        type_characteristic: str,
        game: Game,
        card_key: str,
    ) -> None:
        type_interaction = card_key.split("_")[2]
        game_personages = game.personages.all()
        if type_characteristic == "age":
            num_interaction = int(card_key.split("_")[3])
            for personage in game_personages:
                self.update_age(personage, num_interaction, type_interaction)
        else:
            characteristics = [
                getattr(personage, type_characteristic) for personage in game_personages
            ]
            for i, personage in enumerate(game_personages):
                next_index = (i + 1) % len(game_personages)
                setattr(personage, type_characteristic, characteristics[next_index])
                personage.save()

    def handle_another_personage_interactions(
        self,
        type_action: str,
        personage_instance: Personage,
        another_personage: Personage,
        type_characteristic: str,
        showing_characteristic_type: str,
    ) -> None:
        if type_action == "steal":
            characteristic_value = getattr(another_personage, type_characteristic)
            setattr(personage_instance, type_characteristic, characteristic_value)
            personage_instance.save()
            RegenerateCharacteristicService()(
                another_personage,
                type_characteristic,
            )
        elif type_action == "swap":
            characteristics = (
                DEFAULT_CHARACTERISTICS
                if type_characteristic == "all"
                else [type_characteristic]
            )
            self.swap_characteristic(
                personage_instance,
                another_personage,
                characteristics,
            )
        elif type_action == "show":
            characteristic = (
                showing_characteristic_type
                if type_characteristic == "all"
                else type_characteristic
            )
            self.show_characteristic(
                another_personage,
                another_personage.game.uuid,  # type: ignore[union-attr]
                characteristic,
            )

        elif type_action == "fix":
            old_characteristic = getattr(another_personage, type_characteristic)
            if type_characteristic == "phobia":
                old_characteristic.stage = PhobiaStageChoice.INITIAL
            else:
                old_characteristic.is_curable = True
                old_characteristic.degree_percent = 0
            old_characteristic.save()

    def update_age(
        self,
        personage: Personage,
        num_interaction: int,
        type_interaction: str,
    ) -> None:
        if type_interaction == "plus":
            personage.age += num_interaction  # type: ignore[operator]
        else:
            personage.age -= num_interaction  # type: ignore[operator]
        personage.save()

    def swap_characteristic(
        self,
        personage_instance: Personage,
        another_personage: Personage,
        characteristics: Collection[str],
    ) -> None:
        for characteristic in characteristics:
            instance_characteristic = getattr(personage_instance, characteristic)
            another_characteristic = getattr(another_personage, characteristic)
            setattr(personage_instance, characteristic, another_characteristic)
            setattr(another_personage, characteristic, instance_characteristic)
            personage_instance.save()
            another_personage.save()

    def show_characteristic(
        self,
        personage: Personage,
        game_uuid: UUID | Any,
        type_characteristic: str,
    ) -> None:
        value_characteristic = getattr(personage, type_characteristic)
        visibility = CharacteristicVisibility.objects.get(
            personage=personage,
            characteristic_type=type_characteristic,
        )
        visibility.is_hidden = False
        visibility.save()
        self.web_socket_send_characteristic(
            game_uuid,
            personage.id,
            type_characteristic,
            value_characteristic,
        )
