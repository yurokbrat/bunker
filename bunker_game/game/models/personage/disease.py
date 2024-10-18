from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=120, verbose_name="название", unique=True)
    degree = models.IntegerField(verbose_name="процент болезни")
    is_curable = models.BooleanField(default=True, verbose_name="можно вылечить")

    class Meta:
        verbose_name = "болезнь"
        verbose_name_plural = "болезни"

    def __str__(self):
        return f"{self.name} - {self.degree} - {self.is_curable}"
