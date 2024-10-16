from django.db import models


class AdditionalInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")

    class Meta:
        verbose_name = "доп. информация"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
