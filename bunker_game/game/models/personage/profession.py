import uuid

from django.db import models

from bunker_game.game.enums import ExperienceChoice


class Profession(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, verbose_name="профессия")
    experience = models.CharField(
        choices=ExperienceChoice.choices,
        blank=True,
        verbose_name="опыт работы",
        default="",
    )
    additional_skill = models.CharField(
        max_length=150,
        blank=True,
        default="",
        verbose_name="дополнительное умение",
    )
    is_generated = models.BooleanField(default=False, verbose_name="сгенерирована")

    class Meta:
        verbose_name = "профессия"
        verbose_name_plural = "профессии"

    def __str__(self) -> str:
        return f"{self.name}"
