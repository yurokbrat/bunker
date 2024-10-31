from operator import attrgetter

from rest_framework import status

from bunker_game.users.tests.factories import UserFactory


def test_user_list(user_api_client):
    users = UserFactory.create_batch(5)
    users.append(user_api_client.user)
    response = user_api_client.get("/api/users/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == [
        {
            "uuid": f"{user.uuid}",
            "username": user.username,
            "name": user.name,
            "url": f"http://testserver{user.get_absolute_url()}",
            "avatar": user.avatar.url,
        }
        for user in sorted(users, key=attrgetter("last_online"))
    ]
