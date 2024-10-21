import uuid

from django.db import models


class Character(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120, unique=True, verbose_name="название")

    class Meta:
        verbose_name = "характер"
        verbose_name_plural = "характеры"

    def __str__(self):
        return self.name
