from typing import Any

from factory import Faker, SubFactory, post_generation
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from bunker_game.game.enums import GameDurationType
from bunker_game.game.models import Game
from bunker_game.game.tests.factories.bunker_factories import BunkerFactory
from bunker_game.game.tests.factories.catastrophe_factory import CatastropheFactory
from bunker_game.game.tests.factories.personage_factory import PersonageFactory
from bunker_game.users.tests.factories import UserFactory


class GameFactory(DjangoModelFactory):
    creator = SubFactory(UserFactory)
    bunker = SubFactory(BunkerFactory)
    catastrophe = SubFactory(CatastropheFactory)
    num_places = Faker("random_int")
    game_duration_type = FuzzyChoice(GameDurationType.values)
    time_in_bunker = f"{(Faker('random_int'))} месяцев"
    is_active = True

    class Meta:
        model = Game

    @post_generation
    def personages(self: Game, create: bool, *args: Any, **kwargs: Any) -> None:
        if create:
            personages = PersonageFactory.create_batch(size=5)
            self.personages.set(personages)
            self.save()
