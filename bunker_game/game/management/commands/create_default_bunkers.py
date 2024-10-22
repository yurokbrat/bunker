from pathlib import Path
from typing import Any

from django.conf import settings
from django.core.files.base import File
from django.core.management import BaseCommand
from django.db import transaction

from bunker_game.game.models import Bunker, BunkerRoom


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> None:
        bunker_rooms = {
            "Склад боеприпасов": 50,
            "Склад инструментов": 40,
            "Склад металлолома": 60,
            "Гараж с транспортом": 80,
            "Гараж без транспорта": 60,
            "Карцер": 20,
            "Химическая лаборатория": 45,
            "Комната собраний": 35,
            "Медицинский отсек": 25,
            "Оружейная мастерская": 50,
            "Комната хранения оружия": 30,
            "Генераторная": 40,
            "Серверная": 30,
            "Морозильная комната": 25,
            "Пост охранника": 15,
            "Комната управления камерами": 20,
            "Комната с банковскими ячейками": 30,
            "Гидропонная ферма": 50,
            "Теплица": 70,
            "Кабинет психолога/сексолога": 30,
            "Кабинет врача": 25,
            "Комната управления спутниками": 40,
            "Тренажерный зал": 50,
            "Кухня": 35,
            "Склад древесины": 60,
            "Водоочистительная станция": 50,
            "Склад пиротехники": 40,
            "Аккумуляторная": 30,
            "Склад стройматериалов": 60,
            "Склад с кормом для животных": 40,
            "Комната с 3D принтером": 30,
            "Бассейн": 80,
            "Склад электроники": 50,
            "Библиотека": 45,
            "Лаборатория для исследования вирусов": 50,
            "Комната санитарной обработки": 25,
            "Генетическая лаборатория": 50,
            "Экстренная комната с запасом еды на неделю": 35,
            "Грядки и лампы для выращивания": 30,
            "Кислородный генератор": 20,
            "Кузница": 60,
            "Игровая комната с автоматами": 50,
            "Экстренный электрический генератор": 30,
            "Картинная галерея": 45,
            "Музей": 70,
            "Склад документов": 40,
            "Оружейный склад": 50,
            "Ботанический сад": 60,
            "Швейная мастерская": 30,
            "Комната очистки воды": 25,
            "Штаб": 45,
            "Гараж": 80,
            "Автомастерская": 70,
            "Баня": 40,
            "Подвал": 50,
            "Веранда": 25,
        }

        bunker_info = {
            "Советский бункер": {
                "description": "Секретное укрытие, построенное во "
                "времена холодной войны.",
                "file_name": "soviet_bunker.jpg",
            },
            "Бункер времён второй мировой": {
                "description": "Бункер, использовавшийся для защиты от ядерной атаки.",
                "file_name": "bunker_second_world_war.jpg",
            },
            "Шахта": {
                "description": "Подземное хранилище ресурсов и оборудования.",
                "file_name": "mine.jpg",
            },
            "Бункер лаборатории СССР": {
                "description": "Место, где проводились эксперименты во время войны.",
                "file_name": "soviet_laboratory.jpg",
            },
            "Военная база": {
                "description": "Запасной штаб для военного командования.",
                "file_name": "military_base.jpg",
            },
            "Тюрьма": {
                "description": "Тюрьма с высокими стенами.",
                "file_name": "jail.jpg",
            },
            "Правительственный бункер": {
                "description": "Бункер, предназначенный для "
                "защиты высокопоставленных лиц.",
                "file_name": "government.jpg",
            },
            "Поликлиника": {
                "description": "Специально оборудованный пункт для "
                "оказания медицинской помощи.",
                "file_name": "medicine.jpg",
            },
            "Ферма": {
                "description": "Ферма, использующая современные технологии "
                "для сельского хозяйства.",
                "file_name": "farm.jpg",
            },
            "Продуктовый магазин": {
                "description": "Торговая точка, где можно было "
                "купить запасы продовольствия.",
                "file_name": "shop.jpg",
            },
            "Оружейный магазин": {
                "description": "Место для покупки оборудования "
                "для охоты и отдыха на природе.",
                "file_name": "weapon_shop.jpg",
            },
            "Распределительный центр маркетплейса": {
                "description": "Промышленный склад для хранения товаров.",
                "file_name": "marketplace.jpg",
            },
            "Станция метро": {
                "description": "Общедоступное место для работы метро в прошлом.",
                "file_name": "metro.jpg",
            },
            "Банковский склад": {
                "description": "Место для хранения денег и ценностей.",
                "file_name": "bank.jpg",
            },
            "Промышленный завод": {
                "description": "Завод для создания промышленных товаров.",
                "file_name": "factory.jpg",
            },
            "Автосервис": {
                "description": "Сервисный центр для автомобилей.",
                "file_name": "car_service.jpg",
            },
            "Дом культуры": {
                "description": "Место для проведения культурных мероприятий.",
                "file_name": "house_culture.jpg",
            },
            "Санаторий": {
                "description": "Медицинское учреждение для отдыха и восстановления.",
                "file_name": "sanatorium.jpg",
            },
            "Водоочистное сооружение": {
                "description": "Установка для очистки воды.",
                "file_name": "water_cleaner.jpg",
            },
            "Небольшой многоэтажный дом": {
                "description": "Многоэтажное здание для проживания.",
                "file_name": "house.jpg",
            },
            "Частный дом": {
                "description": "Жилое здание для одной семьи.",
                "file_name": "mini_house.jpg",
            },
            "Хозяйственный магазин": {
                "description": "Магазин, продающий товары для домашнего хозяйства.",
                "file_name": "hardware_store.jpg",
            },
        }

        for name, area in bunker_rooms.items():
            BunkerRoom.objects.get_or_create(name=name, area=area)
        self.stdout.write(self.style.SUCCESS("Комнаты бункеров созданы!"))

        for bunker_name, info in bunker_info.items():
            base_file_path = Path(
                "bunkers",
                "default_images",
            )
            image_path = base_file_path / info.pop("file_name")
            with (settings.MEDIA_ROOT / image_path).open("rb") as image_file:
                Bunker.objects.filter(is_generated=False).get_or_create(
                    name=bunker_name,
                    description=info["description"],
                    image=File(image_file),
                )
        self.stdout.write(self.style.SUCCESS("Стандартные бункеры созданы!"))
