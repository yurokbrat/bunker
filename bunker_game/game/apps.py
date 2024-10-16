from django.apps import AppConfig


class GameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bunker_game.game'
    verbose_name = "Игровые модели"
