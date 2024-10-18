from django.db import models

from bunker_game.game.models import Bunker, Catastrophe, Personage
from bunker_game.users.models import User


class Game(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="создатель игры",
        related_name="games_created",
    )
    personages = models.ManyToManyField(
        Personage,
        related_name="games",
        verbose_name="персонажи в игре",
        blank=True,
    )
    bunker = models.ForeignKey(
        Bunker, on_delete=models.SET_NULL, verbose_name="бункер", null=True, blank=True
    )
    catastrophe = models.ForeignKey(
        Catastrophe,
        on_delete=models.SET_NULL,
        verbose_name="катастрофа",
        null=True,
        blank=True,
    )
    date_start = models.DateTimeField(
        auto_created=True, verbose_name="игра создана в ", null=True, blank=True
    )
    date_end = models.DateTimeField(
        null=True, blank=True, verbose_name="игра закончена в"
    )
    is_active = models.BooleanField(default=False, verbose_name="активна")

    class Meta:
        verbose_name = "игра"
        verbose_name_plural = "игры"

    def __str__(self):
        return f"Игра №{self.id}"
