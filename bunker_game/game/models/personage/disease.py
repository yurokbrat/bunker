from django.db import models


class Disease(models.Model):
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

    class Meta:
        verbose_name = "болезнь"
        verbose_name_plural = "болезни"

    def __str__(self):
        return f"{self.name} - {self.degree_percent} - {self.is_curable}"
