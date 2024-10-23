import uuid

from django.db import models


class AdditionalInfo(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, verbose_name="название", unique=True)

    class Meta:
        verbose_name = "доп. информация"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.name
