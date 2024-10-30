import uuid

from django.db import models

from bunker_game.game.models import Personage
from bunker_game.game.models.vote.voting import Voting


class Vote(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    voting = models.ForeignKey(
        Voting,
        verbose_name="голосование",
        on_delete=models.CASCADE,
        related_name="votes",
    )
    voter = models.ForeignKey(
        Personage,
        verbose_name="голосующий",
        on_delete=models.CASCADE,
        related_name="given_vote",
    )
    target = models.ForeignKey(
        Personage,
        verbose_name="кандидат",
        on_delete=models.CASCADE,
        related_name="received_vote",
    )
    created_at = models.DateTimeField(verbose_name="создан в", auto_now_add=True)

    class Meta:
        verbose_name = "голос"
        verbose_name_plural = "голоса"

    def __str__(self) -> str:
        return f"Голос {self.voter} за {self.target}"
