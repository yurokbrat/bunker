from typing import Any

from django.db.models import Count
from rest_framework.generics import get_object_or_404

from bunker_game.game.models import Game, Personage
from bunker_game.game.models.vote import Vote, Voting
from bunker_game.users.models import User
from bunker_game.utils.exceptions import (
    AlreadyVotedError,
    GameStoppedError,
    NoVotesError,
    VotingActiveError,
    VotingStoppedError,
)


class VoteService:
    def start(self, game: Game) -> Voting:
        if not game.is_active:
            raise GameStoppedError
        voting, created = Voting.objects.get_or_create(game=game, is_active=True)  # type: ignore[attr-defined]
        if not created:
            raise VotingActiveError
        return voting

    def vote(self, voting: Voting, user: User, target_uuid: str) -> Vote:
        if not voting.is_active:
            raise VotingStoppedError
        voter = get_object_or_404(Personage, user=user)
        target = get_object_or_404(Personage, uuid=target_uuid)
        vote, created = Vote.objects.get_or_create(  # type: ignore[attr-defined]
            voting=voting,
            voter=voter,
            target=target,
        )
        if not created:
            raise AlreadyVotedError
        return vote

    def stop(self, voting: Voting) -> tuple[Personage, Any | None]:
        if not voting.is_active:
            raise VotingStoppedError

        vote_counts = (
            Vote.objects.filter(voting=voting)  # type: ignore[attr-defined]
            .values("target")
            .annotate(vote_count=Count("target"))
        )
        if eliminated_candidate := max(
            vote_counts,
            key=lambda x: x["vote_count"],
            default=None,
        ):
            target_id = eliminated_candidate["target"]
            vote_count = eliminated_candidate["vote_count"]
            target_personage = get_object_or_404(Personage, id=target_id)
        else:
            raise NoVotesError

        voting.is_active = False
        voting.save()

        return target_personage, vote_count if eliminated_candidate else None
