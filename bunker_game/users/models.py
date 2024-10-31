import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from bunker_game.utils.generate_hide_name import upload_to_avatars


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(blank=True, max_length=255, verbose_name="имя пользователя")
    avatar = models.ImageField(
        blank=True,
        upload_to=upload_to_avatars,
        verbose_name="аватар",
        default="user-avatars/default.png",
    )
    last_online = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="последнее посещение",
    )
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def get_absolute_url(self) -> str:
        return reverse("users:user-detail", args=(self.uuid,))
