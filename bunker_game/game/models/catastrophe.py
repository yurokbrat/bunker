import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from bunker_game.utils.generate_hide_name import upload_to_catastrophes


class Catastrophe(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.CharField(max_length=250, verbose_name="описание")
    image = models.ImageField(
        upload_to=upload_to_catastrophes,
        verbose_name="фотография",
    )
    impact_level = models.IntegerField(
        default=1,
        verbose_name="масштаб катастрофы",
        help_text="Урон катастрофы по пятибалльной шкале",
        validators=(MinValueValidator(1), MaxValueValidator(5)),
    )

    class Meta:
        verbose_name = "катастрофа"
        verbose_name_plural = "катастрофы"

    def __str__(self):
        return self.name
