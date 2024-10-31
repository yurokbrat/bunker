from rest_framework import status


def test_personage_detail(user_api_client, personage):
    response = user_api_client.get(f"/api/personages/{personage.uuid}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
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
            "degree_percent": personage.disease.degree_percent,
            "is_curable": personage.disease.is_curable,
        },
        "profession": {
            "uuid": f"{personage.profession.uuid}",
            "name": personage.profession.name,
            "additional_skill": personage.profession.additional_skill,
            "experience": personage.profession.experience,
        },
        "phobia": {
            "uuid": f"{personage.phobia.uuid}",
            "name": personage.phobia.name,
            "stage": personage.phobia.stage,
        },
        "hobby": {
            "uuid": f"{personage.hobby.uuid}",
            "name": personage.hobby.name,
            "experience": personage.hobby.experience,
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
            "status": personage.baggage.status,
        },
        "action_cards": [
            {
                "uuid": f"{action_card_usage.uuid}",
                "card": {
                    "uuid": f"{action_card_usage.card.uuid}",
                    "name": action_card_usage.card.name,
                    "key": action_card_usage.card.key,
                    "description": action_card_usage.card.description,
                    "target": action_card_usage.card.target,
                },
                "is_used": action_card_usage.is_used,
            }
            for action_card_usage in personage.action_cards.all()
        ],
    }
