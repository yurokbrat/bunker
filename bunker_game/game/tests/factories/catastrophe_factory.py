from factory import Faker
from factory.django import DjangoModelFactory, ImageField

from bunker_game.game.models import Catastrophe


class CatastropheFactory(DjangoModelFactory):
    name = Faker("name", locale="ru")
    description = Faker("text", locale="ru", max_nb_chars=500)
    image = ImageField()
    impact_level = Faker("pyint", min_value=0, max_value=5)
    percent_population = Faker("pyint", min_value=0, max_value=100)

    class Meta:
        model = Catastrophe
