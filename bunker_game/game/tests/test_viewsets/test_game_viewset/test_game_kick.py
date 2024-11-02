from rest_framework import status


def test_game_kick(creator_game_user_api_client, game):
    response = creator_game_user_api_client.post(
        f"/api/games/{game.uuid}/kick/",
        data={"personage_uuid": game.personages.first().uuid},
    )

    assert response.status_code == status.HTTP_200_OK


def test_game_kick_no_creator_user(gaming_user_api_client, game):
    response = gaming_user_api_client.post(
        f"/api/games/{game.uuid}/kick/",
        data={"personage_uuid": game.personages.first().uuid},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action.",
    }
