from rest_framework import status

from bunker_game.game.models.vote import Voting


def test_voting_start(creator_game_user_api_client, game):
    response = creator_game_user_api_client.post(
        f"/api/games/{game.uuid}/voting/start/",
    )
    voting = Voting.objects.get(game=game)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "uuid": f"{voting.uuid}",
        "game": f"{game.uuid}",
        "votes": [],
        "is_active": voting.is_active,
        "created_at": voting.created_at.astimezone().isoformat(),
    }


def test_voting_start_no_creator_game(user_api_client, game):
    response = user_api_client.post(f"/api/games/{game.uuid}/voting/start/")

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {"detail": "Вы не являетесь создателем игры"}
