from typing import Any

from django.core.management import BaseCommand
from django.db import transaction

from bunker_game.game.constants import ActionCardTargetChoice
from bunker_game.game.models import ActionCard


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> None:
        action_cards = [
            {
                "name": "Украсть болезнь у другого игрока",
                "key": "steal_disease",
                "description": "Вы можете украсть болезнь у любого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Раскрыть характеристику игрока",
                "key": "reveal_any",
                "description": "Вы можете раскрыть любую характеристику любого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Украсть хобби у другого игрока",
                "key": "steal_hobby",
                "description": "Вы можете украсть хобби у любого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Около бункера склад с оружием",
                "key": "info_weapon_storage",
                "description": "Возле вашего бункера находится склад с оружием.",
                "target": ActionCardTargetChoice.GAME
            },
            {
                "name": "Обменяться багажом с другим игроком",
                "key": "trade_baggage",
                "description": "Вы можете обменяться багажом с любым игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Источник воды около бункера",
                "key": "info_freshwater_lake",
                "description": "Теперь ваш бункер находится рядом с источником пресной воды.",
                "target": ActionCardTargetChoice.GAME
            },
            {
                "name": "+1 слот в бункере",
                "key": "increase_bunker_place",
                "description": "Увеличьте количество мест в бункере на 1.",
                "target": ActionCardTargetChoice.GAME
            },
            {
                "name": "-1 слот в бункере",
                "key": "decrease_bunker_place",
                "description": "Уменьшите количество мест в бункере на 1.",
                "target": ActionCardTargetChoice.GAME
            },
            {
                "name": "Защита от выбывания",
                "key": "immunity_one_turn",
                "description": "Получите защиту от выбывания на 1 ход.",
                "target": ActionCardTargetChoice.GAME
            },
            {
                "name": "Украсть багаж у другого игрока",
                "key": "steal_baggage",
                "description": "Украдите багаж у любого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Аннулировать голоса за себя",
                "key": "nullify_votes",
                "description": "Аннулируйте все голоса за себя.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Изменить профессию",
                "key": "change_profession",
                "description": "Вы можете изменить свою профессию на любую.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Вылечить игрока от болезни",
                "key": "heal_disease",
                "description": "Вылечите любого игрока от болезни.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Вылечить свою фобию",
                "key": "heal_phobia",
                "description": "Вы можете вылечить свою фобию.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Обмен профессиями по кругу",
                "key": "swap_professions_all",
                "description": "Все игроки меняются профессиями по часовой стрелке.",
                "target": ActionCardTargetChoice.ALL
            },
            {
                "name": "Поменять ориентацию",
                "key": "change_orientation",
                "description": "Вы можете изменить свою ориентацию.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Раскрыть болезнь игрока",
                "key": "reveal_disease",
                "description": "Раскройте состояние болезни любого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Перегенерировать профессию",
                "key": "regenerate_profession",
                "description": "Вы можете перегенерировать свою профессию.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Перегенерировать болезнь",
                "key": "regenerate_disease",
                "description": "Вы можете перегенерировать свою болезнь.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Перегенерировать фобию",
                "key": "regenerate_phobia",
                "description": "Вы можете перегенерировать свою фобию.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Перегенерировать хобби",
                "key": "regenerate_hobby",
                "description": "Вы можете перегенерировать своё хобби.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Поменяться возрастом с другим игроком",
                "key": "swap_age",
                "description": "Вы можете поменяться возрастом с любым игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Украсть профессию у другого игрока",
                "key": "steal_profession",
                "description": "Вы можете украсть профессию у другого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Раскрыть фобию игрока",
                "key": "reveal_phobia",
                "description": "Раскройте фобию любого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Изменить пол",
                "key": "change_gender",
                "description": "Вы можете изменить свой пол.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Обменяться багажом с другим игроком",
                "key": "swap_baggage",
                "description": "Вы можете обменяться багажом с любым игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Перегенерировать эпидемию вокруг бункера",
                "key": "regenerate_epidemic",
                "description": "Перегенерируйте эпидемию вокруг вашего бункера.",
                "target": ActionCardTargetChoice.GAME
            },
            {
                "name": "Раскрыть тайную характеристику",
                "key": "reveal_secret",
                "description": "Раскройте одну не озвученную характеристику любого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            },
            {
                "name": "Уменьшить возраст на 10 лет",
                "key": "decrease_age",
                "description": "Вы можете уменьшить свой возраст на 10 лет.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Увеличить возраст на 10 лет",
                "key": "increase_age",
                "description": "Вы можете увеличить свой возраст на 10 лет.",
                "target": ActionCardTargetChoice.MYSELF
            },
            {
                "name": "Перегенерировать количество мест в бункере",
                "key": "regenerate_bunker_slots",
                "description": "Перегенерируйте количество мест в вашем бункере.",
                "target": ActionCardTargetChoice.GAME
            },
            {
                "name": "Поменяться всеми характеристиками с игроком",
                "key": "swap_all_characteristics",
                "description": "Поменяйтесь всеми характеристиками с другим игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE
            }
        ]

        for action_card_data in action_cards:
            ActionCard.objects.get_or_create(name=action_card_data["name"], defaults=action_card_data)
        self.stdout.write(self.style.SUCCESS("... Карты действий созданы ... "))



