from typing import Any

from django.core.management import BaseCommand
from django.db import transaction

from bunker_game.game.enums import ActionCardTargetChoice
from bunker_game.game.models import ActionCard


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> None:
        action_cards = [
            #  Another personage interactions
            {
                "name": "Украсть болезнь",
                "key": "steal_disease",
                "description": "Вы можете украсть болезнь любого игрока. "
                "Новая болезнь игрока будет сгенерирована автоматически.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Украсть хобби",
                "key": "steal_hobby",
                "description": "Вы можете украсть хобби любого игрока. "
                "Новое хобби игрока будет сгенерировано автоматически.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Украсть багаж",
                "key": "steal_baggage",
                "description": "Украдите багаж любого игрока. "
                "Новый багаж игрока будет сгенерирован автоматически.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Украсть профессию",
                "key": "steal_profession",
                "description": "Вы можете украсть профессию другого игрока. "
                "Новая профессия игрока будет сгенерирована автоматически.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Украсть возраст",
                "key": "steal_age",
                "description": "Вы можете украсть возраст другого игрока. "
                "Новый возраст игрока будет сгенерирован автоматически.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Украсть пол",
                "key": "steal_age",
                "description": "Вы можете украсть пол другого игрока. "
                "Новый пол игрока будет сгенерирован автоматически.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Обменяться болезнью",
                "key": "swap_disease",
                "description": "Вы можете обменяться болезнью с любым игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Обменяться хобби",
                "key": "swap_hobby",
                "description": "Вы можете обменяться хобби с любым игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Обменяться багажом",
                "key": "swap_baggage",
                "description": "Обменяйте багаж с другим игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Обменяться профессией",
                "key": "swap_profession",
                "description": "Вы можете обменять профессию с другим игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Обменяться возрастом",
                "key": "swap_age",
                "description": "Вы можете обменять возраст с другим игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Обменяться полом",
                "key": "swap_gender",
                "description": "Вы можете обменять пол с другим игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Поменяться всеми характеристиками",
                "key": "swap_all_characteristics",
                "description": "Поменяйтесь всеми характеристиками с другим игроком.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Раскрыть болезнь",
                "key": "show_disease",
                "description": "Раскройте болезнь любого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Раскрыть фобию",
                "key": "show_phobia",
                "description": "Раскройте фобию любого игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Раскрыть тайную характеристику",
                "key": "show_any",
                "description": "Раскройте любую неозвученную характеристику другого "
                "игрока.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Вылечить игрока",
                "key": "fix_disease",
                "description": "Вылечите любого игрока от болезни.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            {
                "name": "Уменьшить стадию фобии",
                "key": "fix_phobia",
                "description": "Вы можете изменить стадию фобии другого "
                "игрока на начальную.",
                "target": ActionCardTargetChoice.ANOTHER_PERSONAGE,
            },
            #  Myself interactions
            {
                "name": "Перегенерировать профессию",
                "key": "regenerate_profession",
                "description": "Вы можете перегенерировать свою профессию.",
                "target": ActionCardTargetChoice.MYSELF,
            },
            {
                "name": "Перегенерировать болезнь",
                "key": "regenerate_disease",
                "description": "Вы можете перегенерировать свою болезнь.",
                "target": ActionCardTargetChoice.MYSELF,
            },
            {
                "name": "Перегенерировать фобию",
                "key": "regenerate_phobia",
                "description": "Вы можете перегенерировать свою фобию.",
                "target": ActionCardTargetChoice.MYSELF,
            },
            {
                "name": "Перегенерировать хобби",
                "key": "regenerate_hobby",
                "description": "Вы можете перегенерировать своё хобби.",
                "target": ActionCardTargetChoice.MYSELF,
            },
            {
                "name": "Изменить пол",
                "key": "regenerate_gender",
                "description": "Вы можете изменить свой пол.",
                "target": ActionCardTargetChoice.MYSELF,
            },
            {
                "name": "Уменьшить возраст на 10 лет",
                "key": "fix_age_minus_10",
                "description": "Вы можете уменьшить свой возраст на 10 лет.",
                "target": ActionCardTargetChoice.MYSELF,
            },
            {
                "name": "Увеличить возраст на 10 лет",
                "key": "fix_age_plus_10",
                "description": "Вы можете увеличить свой возраст на 10 лет.",
                "target": ActionCardTargetChoice.MYSELF,
            },
            {
                "name": "Уменьшить процент болезни на 20%",
                "key": "fix_disease_minus_20",
                "description": "Вы можете уменьшить процент своей болезни на 20%.",
                "target": ActionCardTargetChoice.MYSELF,
            },
            #  Game interactions
            {
                "name": "Около бункера обнаружен склад с оружием",
                "key": "info_weapon_storage",
                "description": "Возле вашего бункера находится склад с оружием.",
                "target": ActionCardTargetChoice.GAME,
            },
            {
                "name": "Около бункера обнаружена больница",
                "key": "info_hospital",
                "description": "Возле вашего бункера находится заброшенная больница "
                "с запасом медикаментов. Теперь вы можете вылечить одного игрока",
                "target": ActionCardTargetChoice.GAME,
            },
            {
                "name": "Недалеко обнаружен дружественный бункер",
                "key": "info_another_friendly_bunker",
                "description": "Возле вашего бункера находится бункер "
                "с двумя здоровыми мужчинами возрастом от 18 до 30 лет.",
                "target": ActionCardTargetChoice.GAME,
            },
            {
                "name": "Рядом обнаружен враждебный бункер",
                "key": "info_another_hostile_bunker",
                "description": "Возле вашего бункера находится бункер, "
                "который настроен агрессивно",
                "target": ActionCardTargetChoice.GAME,
            },
            {
                "name": "Источник воды появился около бункера",
                "key": "info_freshwater_lake",
                "description": "Теперь ваш бункер находится рядом с источником "
                "пресной воды.",
                "target": ActionCardTargetChoice.GAME,
            },
            {
                "name": "+1 слот в бункере",
                "key": "edit_bunker_num_places_plus_one",
                "description": "Увеличьте количество мест в бункере на 1.",
                "target": ActionCardTargetChoice.GAME,
            },
            {
                "name": "-1 слот в бункере",
                "key": "edit_bunker_num_places_minus_one",
                "description": "Уменьшите количество мест в бункере на 1.",
                "target": ActionCardTargetChoice.GAME,
            },
            {
                "name": "Перегенерировать эпидемию",
                "key": "regenerate_catastrophe",
                "description": "Перегенерируйте эпидемию вокруг вашего бункера.",
                "target": ActionCardTargetChoice.GAME,
            },
            {
                "name": "Перегенерировать бункер",
                "key": "regenerate_bunker",
                "description": "Перегенерируйте бункер.",
                "target": ActionCardTargetChoice.GAME,
            },
            #  All interactions
            {
                "name": "Обмен профессиями по кругу",
                "key": "change_profession_clockwise",
                "description": "Все игроки меняются профессиями по часовой стрелке.",
                "target": ActionCardTargetChoice.ALL,
            },
            {
                "name": "Обмен фобиями по кругу",
                "key": "change_phobia_clockwise",
                "description": "Все игроки меняются фобиями по часовой стрелке.",
                "target": ActionCardTargetChoice.ALL,
            },
            {
                "name": "Увеличить возраст всех игроков на 10",
                "key": "change_age_plus_10",
                "description": "Возраст всех игроков увеличивается на 10.",
                "target": ActionCardTargetChoice.ALL,
            },
            {
                "name": "Уменьшить возраст всех игроков на 10",
                "key": "change_age_minus_10",
                "description": "Возраст всех игроков уменьшается на 10.",
                "target": ActionCardTargetChoice.ALL,
            },
        ]

        for action_card_data in action_cards:
            ActionCard.objects.get_or_create(
                name=action_card_data["name"],
                defaults=action_card_data,
            )
        self.stdout.write(self.style.SUCCESS("... Карты действий созданы ... "))
