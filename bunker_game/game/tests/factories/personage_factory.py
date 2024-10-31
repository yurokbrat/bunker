from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from bunker_game.game.enums import GenderChoice, OrientationChoice
from bunker_game.game.models import Personage
from bunker_game.game.tests.factories.characteristics_factories import (
    AdditionalInfoFactory,
    BaggageFactory,
    CharacterFactory,
    DiseaseFactory,
    HobbyFactory,
    PhobiaFactory,
    ProfessionFactory,
)
from bunker_game.users.tests.factories import UserFactory


class PersonageFactory(DjangoModelFactory):
    user = SubFactory(UserFactory)
    age = Faker("pyint", min_value=1, max_value=100)
    gender = FuzzyChoice(GenderChoice.values)
    orientation = FuzzyChoice(OrientationChoice.values)
    disease = SubFactory(DiseaseFactory)
    profession = SubFactory(ProfessionFactory)
    phobia = SubFactory(PhobiaFactory)
    hobby = SubFactory(HobbyFactory)
    character = SubFactory(CharacterFactory)
    additional_info = SubFactory(AdditionalInfoFactory)
    baggage = SubFactory(BaggageFactory)

    class Meta:
        model = Personage
