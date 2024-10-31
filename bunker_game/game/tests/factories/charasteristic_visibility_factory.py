from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from bunker_game.game.enums import TypeCharacteristicChoices
from bunker_game.game.models import CharacteristicVisibility
from bunker_game.game.tests.factories.personage_factory import PersonageFactory


class CharacteristicVisibilityFactory(DjangoModelFactory):
    personage = SubFactory(PersonageFactory)
    characteristic_type = FuzzyChoice(TypeCharacteristicChoices.values)

    class Meta:
        model = CharacteristicVisibility
