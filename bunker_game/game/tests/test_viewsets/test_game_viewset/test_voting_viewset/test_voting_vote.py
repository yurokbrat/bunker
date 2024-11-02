from rest_framework import status

from bunker_game.game.models.vote import Vote
from bunker_game.game.tests.factories import VoteFactory


def test_voting_vote(gaming_user_api_client, game, voting):
    target_personage = game.personages.first()
    response = gaming_user_api_client.post(
        f"/api/games/{game.uuid}/voting/{voting.uuid}/vote/",
        data={"target": target_personage.uuid},
    )
    vote = Vote.objects.get(voting=voting, target=target_personage)  # type: ignore[attr-defined]

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        "uuid": f"{vote.uuid}",
        "voter": {
            "uuid": f"{vote.voter.uuid}",
            "user": {
                "uuid": f"{vote.voter.user.uuid}",
                "username": vote.voter.user.username,
                "name": vote.voter.user.name,
                "url": f"http://testserver{vote.voter.user.get_absolute_url()}",
                "avatar": vote.voter.user.avatar.url,
            },
            "age": vote.voter.age,
            "gender": vote.voter.gender,
            "orientation": vote.voter.orientation,
            "disease": {
                "uuid": f"{vote.voter.disease.uuid}",
                "name": vote.voter.disease.name,
            },
            "profession": {
                "uuid": f"{vote.voter.profession.uuid}",
                "name": vote.voter.profession.name,
            },
            "phobia": {
                "uuid": f"{vote.voter.phobia.uuid}",
                "name": vote.voter.phobia.name,
            },
            "hobby": {
                "uuid": f"{vote.voter.hobby.uuid}",
                "name": vote.voter.hobby.name,
            },
            "character": {
                "uuid": f"{vote.voter.character.uuid}",
                "name": vote.voter.character.name,
            },
            "additional_info": {
                "uuid": f"{vote.voter.additional_info.uuid}",
                "name": vote.voter.additional_info.name,
            },
            "baggage": {
                "uuid": f"{vote.voter.baggage.uuid}",
                "name": vote.voter.baggage.name,
            },
        },
        "target": {
            "uuid": f"{vote.target.uuid}",
            "user": {
                "uuid": f"{vote.target.user.uuid}",
                "username": vote.target.user.username,
                "name": vote.target.user.name,
                "url": f"http://testserver{vote.target.user.get_absolute_url()}",
                "avatar": vote.target.user.avatar.url,
            },
            "age": vote.target.age,
            "gender": vote.target.gender,
            "orientation": vote.target.orientation,
            "disease": {
                "uuid": f"{vote.target.disease.uuid}",
                "name": vote.target.disease.name,
            },
            "profession": {
                "uuid": f"{vote.target.profession.uuid}",
                "name": vote.target.profession.name,
            },
            "phobia": {
                "uuid": f"{vote.target.phobia.uuid}",
                "name": vote.target.phobia.name,
            },
            "hobby": {
                "uuid": f"{vote.target.hobby.uuid}",
                "name": vote.target.hobby.name,
            },
            "character": {
                "uuid": f"{vote.target.character.uuid}",
                "name": vote.target.character.name,
            },
            "additional_info": {
                "uuid": f"{vote.target.additional_info.uuid}",
                "name": vote.target.additional_info.name,
            },
            "baggage": {
                "uuid": f"{vote.target.baggage.uuid}",
                "name": vote.target.baggage.name,
            },
        },
        "created_at": vote.created_at.astimezone().isoformat(),
    }


def test_voting_vote_another_user(user_api_client, game, voting):
    target_personage = game.personages.first()
    response = user_api_client.post(
        f"/api/games/{game.uuid}/voting/{voting.uuid}/vote/",
        data={"target": target_personage.uuid},
    )

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action.",
    }


def test_stopped_voting_vote(gaming_user_api_client, game, voting):
    voting.is_active = False
    voting.save()
    target_personage = game.personages.first()
    response = gaming_user_api_client.post(
        f"/api/games/{game.uuid}/voting/{voting.uuid}/vote/",
        data={"target": target_personage.uuid},
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"detail": "Голосование уже завершено"}


def test_voting_dublicate_vote(gaming_user_api_client, game, gaming_personage, voting):
    target_personage = game.personages.first()
    vote = VoteFactory(voting=voting, voter=gaming_personage, target=target_personage)
    voting.votes.add(vote)
    voting.save()
    response = gaming_user_api_client.post(
        f"/api/games/{game.uuid}/voting/{voting.uuid}/vote/",
        data={"target": target_personage.uuid},
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"detail": "Вы уже проголосовали"}
