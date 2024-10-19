from django.db import models


class GenderChoice(models.TextChoices):
    MALE = "male", "Мужчина"
    FEMALE = "female", "Женщина"


class OrientationChoice(models.TextChoices):
    HOMOSEXUAL = "homosexual", "Гомосексуален"
    ASEXUAL = "asexual", "Асексуален"
    HETEROSEXUAL = "heterosexual", "Гетеросексуален"


class PhobiaStageChoice(models.TextChoices):
    NONE = "none", "Отсутствует"
    MILD = "mild", "Легкая"
    MODERATE = "moderate", "Средняя"
    SEVERE = "severe", "Серьезная"
    PANIC = "panic", "Паническая"


class StatusBaggageChoice(models.TextChoices):
    INTACT = "intact", "Целый"
    DAMAGED = "damaged", "Поврежденный"


class ExperienceChoice(models.TextChoices):
    NOVICE = "novice", "Новичок"
    AMATEUR = "amateur", "Любитель"
    EXPERIENCED = "experienced", "Опытный"
    PROFESSIONAL = "professional", "Профессионал"
    MASTER = "master", "Мастер"


class TypeCharacteristic(models.TextChoices):
    AGE = "age", "Возраст"
    GENDER = "gender", "Пол"
    ORIENTATION = "orientation", "Ориентация"
    DISEASE = "disease", "Здоровье"
    PROFESSION = "profession", "Профессия"
    PHOBIA = "phobia", "Фобия"
    HOBBY = "hobby", "Хобби"
    CHARACTER = "character", "Характер"
    ADDITIONAL_INFO = "additional_info", "Доп. Информация"
    BAGGAGE = "baggage", "Багаж"


class ActionCardTargetChoice(models.TextChoices):
    ALL = "all", "Все персонажи"
    MYSELF = "myself", "На себя"
    ANOTHER_PERSONAGE = "another_personage", "Другой персонаж"
    GAME = "game", "Игра"
