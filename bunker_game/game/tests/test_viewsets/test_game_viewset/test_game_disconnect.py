from rest_framework import status


def test_game_disconnect(gaming_user_api_client, game):
    response = gaming_user_api_client.delete(f"/api/games/{game.uuid}/disconnect/")

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_game_disconnect_another_user(user_api_client, game):
    response = user_api_client.delete(f"/api/games/{game.uuid}/disconnect/")

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action.",
    }
