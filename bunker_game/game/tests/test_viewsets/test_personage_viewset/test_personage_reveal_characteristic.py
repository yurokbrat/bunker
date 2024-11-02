import pytest
from rest_framework import status

from bunker_game.game.tests.utils import generate_model_expected_data


@pytest.mark.parametrize(
    "characteristic_type",
    [
        "age",
        "gender",
        "orientation",
    ],
)
def test_personage_reveal_usual_characteristic(
    user_api_client,
    personage,
    game,
    characteristic_type,
):
    personage.user = user_api_client.user
    personage.game = game
    personage.save()

    response = user_api_client.patch(
        f"/api/personages/{personage.uuid}/reveal-characteristic/",
        data={"characteristic_type": characteristic_type},
    )
    characteristic_value = getattr(personage, characteristic_type)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "characteristic_type": characteristic_type,
        "characteristic_value": characteristic_value,
        "is_hidden": False,
    }


@pytest.mark.parametrize(
    "characteristic_type",
    [
        "disease",
        "profession",
        "phobia",
        "hobby",
        "character",
        "additional_info",
        "baggage",
    ],
)
def test_personage_reveal_model_characteristic(
    user_api_client,
    personage,
    game,
    characteristic_type,
):
    personage.user = user_api_client.user
    personage.game = game
    personage.save()

    response = user_api_client.patch(
        f"/api/personages/{personage.uuid}/reveal-characteristic/",
        data={"characteristic_type": characteristic_type},
    )
    characteristic_value = getattr(personage, characteristic_type)
    expected_data = generate_model_expected_data(
        characteristic_type,
        characteristic_value,
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "characteristic_type": characteristic_type,
        "characteristic_value": expected_data[characteristic_type],
        "is_hidden": False,
    }


def test_personage_reveal_nonexistent_characteristic(user_api_client, personage, game):
    personage.user = user_api_client.user
    personage.game = game
    personage.save()

    response = user_api_client.patch(
        f"/api/personages/{personage.uuid}/reveal-characteristic/",
        data={"characteristic_type": "nonexistent"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {
        "characteristic_type": ['"nonexistent" is not a valid choice.'],
    }


def test_personage_reveal_characteristic_another_user(user_api_client, personage, game):
    personage.game = game
    personage.save()

    response = user_api_client.patch(
        f"/api/personages/{personage.uuid}/reveal-characteristic/",
        data={"characteristic_type": "age"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action.",
    }
