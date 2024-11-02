from rest_framework import status


def test_voting_stop(creator_game_user_api_client, game, voting_with_votes, personage):
    game.personages.add(personage)
    game.save()
    response = creator_game_user_api_client.post(
        f"/api/games/{game.uuid}/voting/{voting_with_votes.uuid}/stop/",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        "results": {
            "personage": {
                "uuid": f"{personage.uuid}",
                "user": {
                    "uuid": f"{personage.user.uuid}",
                    "username": personage.user.username,
                    "name": personage.user.name,
                    "url": f"http://testserver{personage.user.get_absolute_url()}",
                    "avatar": personage.user.avatar.url,
                },
                "age": personage.age,
                "gender": personage.gender,
                "orientation": personage.orientation,
                "disease": {
                    "uuid": f"{personage.disease.uuid}",
                    "name": personage.disease.name,
                },
                "profession": {
                    "uuid": f"{personage.profession.uuid}",
                    "name": personage.profession.name,
                },
                "phobia": {
                    "uuid": f"{personage.phobia.uuid}",
                    "name": personage.phobia.name,
                },
                "hobby": {
                    "uuid": f"{personage.hobby.uuid}",
                    "name": personage.hobby.name,
                },
                "character": {
                    "uuid": f"{personage.character.uuid}",
                    "name": personage.character.name,
                },
                "additional_info": {
                    "uuid": f"{personage.additional_info.uuid}",
                    "name": personage.additional_info.name,
                },
                "baggage": {
                    "uuid": f"{personage.baggage.uuid}",
                    "name": personage.baggage.name,
                },
            },
            "vote_count": voting_with_votes.votes.count(),
        },
    }


def test_voting_stop_no_creator_game(gaming_user_api_client, game, voting_with_votes):
    response = gaming_user_api_client.post(
        f"/api/games/{game.uuid}/voting/{voting_with_votes.uuid}/stop/",
    )

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action.",
    }
