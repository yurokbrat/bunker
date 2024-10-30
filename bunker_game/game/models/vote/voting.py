import uuid

from django.db import models

from bunker_game.game.models import Game


class Voting(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    game = models.ForeignKey(
        Game,
        verbose_name="игра",
        on_delete=models.CASCADE,
        related_name="voting",
    )
    is_active = models.BooleanField(default=True, verbose_name="активно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="начато в")

    class Meta:
        verbose_name = "голосование"
        verbose_name_plural = "голосования"

    def __str__(self) -> str:
        return f"Голосование в игре {self.game.uuid}"
