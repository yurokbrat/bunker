from django.db import models

from bunker_game.game.models.constants import ExperienceChoice


class Profession(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="профессия")
    experience = models.CharField(
        choices=ExperienceChoice.choices,
        verbose_name="опыт работы",
    )

    class Meta:
        verbose_name = "профессия"
        verbose_name_plural = "профессии"

    def __str__(self):
        return self.name
