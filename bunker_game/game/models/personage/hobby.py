from django.db import models

from bunker_game.game.constants import ExperienceChoice


class Hobby(models.Model):
    name = models.CharField(max_length=120, verbose_name="название")
    experience = models.CharField(
        choices=ExperienceChoice.choices,
        verbose_name="опыт хобби",
        blank=True,
    )

    class Meta:
        verbose_name = "хобби"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name} - {self.experience}"
