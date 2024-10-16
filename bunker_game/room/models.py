from django.db import models

from bunker_game.users.models import User


class Room(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="создатель комнаты",
        related_name="room_creator",
        blank=True,
        null=True,
    )
    is_started = models.BooleanField(verbose_name="игра начата", default=False)
    date_start = models.DateTimeField(auto_created=True, verbose_name="игра создана в ")

    class Meta:
        verbose_name = "комната"
        verbose_name_plural = "комнаты"

    def __str__(self):
        return f"Комната №{self.id} | Создатель – {self.creator}"
