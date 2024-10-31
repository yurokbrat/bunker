from rest_framework import status

from bunker_game.game.tests.factories import PersonageFactory


def test_personage_list(user_api_client):
    personages = PersonageFactory.create_batch(5)
    response = user_api_client.get("/api/personages/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == [
        {
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
        }
        for personage in personages
    ]
