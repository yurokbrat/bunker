from django.db import models

from bunker_game.game.constants.type_card import TypeCard


class Card(models.Model):
    name = models.CharField(max_length=120, verbose_name="название")
    type = models.CharField(choices=TypeCard.choices, verbose_name="тип карточки")

    class Meta:
        verbose_name = "карточка"
        verbose_name_plural = "карточки"

    def __str__(self):
        return self.name
