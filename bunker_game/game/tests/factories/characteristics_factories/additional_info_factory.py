from factory import Faker
from factory.django import DjangoModelFactory

from bunker_game.game.models import AdditionalInfo


class AdditionalInfoFactory(DjangoModelFactory):
    name = Faker("name", locale="ru")

    class Meta:
        model = AdditionalInfo
