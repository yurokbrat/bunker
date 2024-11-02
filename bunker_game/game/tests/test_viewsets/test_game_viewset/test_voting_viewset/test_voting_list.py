from rest_framework import status

from bunker_game.game.tests.factories import VotingFactory


def test_voting_list(gaming_user_api_client, game):
    voting_list = VotingFactory.create_batch(5, game=game)
    response = gaming_user_api_client.get(f"/api/games/{game.uuid}/voting/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(voting_list)
    assert response.data == [
        {
            "uuid": f"{voting.uuid}",
            "game": f"{game.uuid}",
            "votes": [
                {
                    "uuid": f"{voting.uuid}",
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
                for vote in voting.votes.all()
            ],
            "is_active": voting.is_active,
            "created_at": voting.created_at.astimezone().isoformat(),
        }
        for voting in voting_list
    ]
