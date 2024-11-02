from rest_framework import status


def test_game_stop(creator_game_user_api_client, game):
    response = creator_game_user_api_client.post(f"/api/games/{game.uuid}/stop/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"result": "Игра завершена"}


def test_game_stop_no_creator(user_api_client, game):
    response = user_api_client.post(f"/api/games/{game.uuid}/stop/")

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action.",
    }
