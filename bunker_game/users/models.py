from django.contrib.auth.models import AbstractUser
from django.db import models

from bunker_game.utils.generate_hide_name import upload_to_avatars


class User(AbstractUser):
    name = models.CharField(blank=True, max_length=255, verbose_name="имя пользователя")
    avatar = models.ImageField(blank=True, upload_to=upload_to_avatars, verbose_name="аватар")
    last_online = models.DateTimeField(blank=True, null=True, verbose_name="последнее посещение")
    room = models.ForeignKey(
        to="room.Room",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="комната",
        related_name="users",
    )
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
