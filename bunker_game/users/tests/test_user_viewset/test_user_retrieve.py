from rest_framework import status


def test_user_retrieve(user_api_client):
    user = user_api_client.user
    response = user_api_client.get(f"/api/users/{user.uuid}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "uuid": f"{user.uuid}",
        "username": user.username,
        "name": user.name,
        "url": f"http://testserver{user.get_absolute_url()}",
        "avatar": user.avatar.url,
        "date_joined": user.date_joined.astimezone().isoformat(),
        "last_online": user.last_online.astimezone().isoformat(),
    }
