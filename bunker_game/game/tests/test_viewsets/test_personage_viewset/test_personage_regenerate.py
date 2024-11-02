import pytest
from rest_framework import status

from bunker_game.game.tests.factories import PersonageFactory
from bunker_game.game.tests.utils import generate_model_expected_data


@pytest.mark.parametrize(
    "characteristic_type",
    [
        "age",
        "gender",
        "orientation",
    ],
)
def test_personage_regenerate_usual_characteristic(
    user_api_client,
    personage,
    characteristic_type,
):
    personage = PersonageFactory()
    personage.user = user_api_client.user
    personage.save()
    response = user_api_client.patch(
        f"/api/personages/{personage.uuid}/regenerate/",
        data={"characteristic_type": characteristic_type},
    )
    personage.refresh_from_db()
    characteristic_value = getattr(personage, characteristic_type)
    expected_data = {characteristic_type: characteristic_value}

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


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
def test_personage_regenerate_model_characteristic(
    user_api_client,
    personage,
    characteristic_type,
):
    personage = PersonageFactory()
    personage.user = user_api_client.user
    personage.save()
    response = user_api_client.patch(
        f"/api/personages/{personage.uuid}/regenerate/",
        data={"characteristic_type": characteristic_type},
    )
    personage.refresh_from_db()
    characteristic_value = getattr(personage, characteristic_type)
    expected_data = generate_model_expected_data(
        characteristic_type,
        characteristic_value,
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


def test_personage_regenerate_nonexistent_characteristic(user_api_client, personage):
    personage.user = user_api_client.user
    personage.save()
    response = user_api_client.patch(
        f"/api/personages/{personage.uuid}/regenerate/",
        data={"characteristic_type": "nonexistent"},
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {
        "characteristic_type": ['"nonexistent" is not a valid choice.'],
    }


def test_personage_regenerate_another_user(user_api_client, personage):
    response = user_api_client.patch(
        f"/api/personages/{personage.uuid}/regenerate/",
        data={"characteristic_type": "age"},
    )

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action.",
    }
