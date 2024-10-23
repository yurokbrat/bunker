from django.urls import resolve, reverse

from bunker_game.users.models import User


def test_user_detail(user: User):
    assert (
        reverse("users:user-detail", kwargs={"uuid": user.uuid})
        == f"/api/users/{user.uuid}/"
    )
    assert resolve(f"/api/users/{user.uuid}/").view_name == "users:user-detail"


def test_user_list():
    assert reverse("users:user-list") == "/api/users/"
    assert resolve("/api/users/").view_name == "users:user-list"


def test_user_me():
    assert reverse("users:user-me") == "/api/users/me/"
    assert resolve("/api/users/me/").view_name == "users:user-me"
