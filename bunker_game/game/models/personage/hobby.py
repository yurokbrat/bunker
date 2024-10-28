import uuid

from django.db import models

from bunker_game.game.enums import ExperienceChoice


class Hobby(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120, verbose_name="название")
    experience = models.CharField(
        choices=ExperienceChoice.choices,
        verbose_name="опыт хобби",
        blank=True,
        default="",
    )
    is_generated = models.BooleanField(default=False, verbose_name="сгенерирована")

    class Meta:
        verbose_name = "хобби"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return f"{self.name}"
