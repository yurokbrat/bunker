import contextlib

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "bunker_game.users"
    verbose_name = "Пользователи"

    def ready(self):
        with contextlib.suppress(ImportError):
            import bunker_game.users.signals  # noqa: F401
