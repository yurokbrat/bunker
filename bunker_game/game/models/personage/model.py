import uuid

from django.db import models

from bunker_game.game.constants import GenderChoice, OrientationChoice
from bunker_game.game.models.personage.additional_info import AdditionalInfo
from bunker_game.game.models.personage.baggage import Baggage
from bunker_game.game.models.personage.character import Character
from bunker_game.game.models.personage.disease import Disease
from bunker_game.game.models.personage.hobby import Hobby
from bunker_game.game.models.personage.phobia import Phobia
from bunker_game.game.models.personage.profession import Profession
from bunker_game.users.models import User


class Personage(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="пользователь",
        null=True,
        blank=True,
    )
    game = models.ForeignKey(
        "game.Game",
        on_delete=models.CASCADE,
        verbose_name="игра",
        related_name="personages_in_game",
        null=True,
        blank=True,
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="возраст",
        blank=True,
        null=True,
    )
    gender = models.CharField(
        choices=GenderChoice.choices,
        blank=True,
        verbose_name="пол",
    )
    orientation = models.CharField(
        choices=OrientationChoice.choices,
        verbose_name="ориентация",
        blank=True,
    )
    disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="болезнь",
    )
    profession = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="профессия",
    )
    phobia = models.ForeignKey(
        Phobia,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="фобия",
    )
    hobby = models.ForeignKey(
        Hobby,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="хобби",
    )
    character = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="характер",
    )
    additional_info = models.ForeignKey(
        AdditionalInfo,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="доп, информация",
    )
    baggage = models.ForeignKey(
        Baggage,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="багаж",
    )

    class Meta:
        verbose_name = "персонаж"
        verbose_name_plural = "персонажи"

    def __str__(self):
        return f"Персонаж {self.user.username}"
