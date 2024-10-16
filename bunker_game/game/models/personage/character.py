from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=120, verbose_name="название")

    class Meta:
        verbose_name = "характер"
        verbose_name_plural = "характеры"

    def __str__(self):
        return self.name
