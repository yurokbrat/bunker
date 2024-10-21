import uuid

from django.db import models


class Disease(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=120, verbose_name="название")
    degree_percent = models.IntegerField(
        verbose_name="процент болезни",
        null=True,
        blank=True,
    )
    is_curable = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="можно вылечить",
    )
    is_generated = models.BooleanField(default=False, verbose_name="сгенерирована")

    class Meta:
        verbose_name = "болезнь"
        verbose_name_plural = "болезни"

    def __str__(self):
        return f"{self.name}"
