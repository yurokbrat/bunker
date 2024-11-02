from factory import Faker
from factory.django import DjangoModelFactory

from bunker_game.game.models import AdditionalInfo


class AdditionalInfoFactory(DjangoModelFactory):
    name = Faker("text", locale="ru", max_nb_chars=100)

    class Meta:
        model = AdditionalInfo
