from django.db import models


class TypeCard(models.TextChoices):
    CATASTROPHE = "catastrophe", "Эпидемия"
    BUNKER_TYPE = "bunker_type", "Тип бункера"
    PROFESSION = "profession", "Профессия"
    GENDER = "gender", "Пол"
    ORIENTATION = "orientation", "Ориентация"
    HEALTH = "health", "Здоровье"
    PHOBIA = "phobia", "Фобия"
    CHARACTER = "character", "Характер"
    HOBBY = "hobby", "Хобби"
    ADDITIONAL_INFO = "add_info", "Доп. Информация"
    ITEM = "item", "Багаж"
