from factory import Faker
from factory.django import DjangoModelFactory

from bunker_game.game.models import Disease


class DiseaseFactory(DjangoModelFactory):
    name = Faker("text", locale="ru", max_nb_chars=120)
    degree_percent = Faker("pyint", min_value=0, max_value=100)
    is_curable = Faker("boolean")

    class Meta:
        model = Disease
