from rest_framework import status


def test_personage_generate(user_api_client, empty_personage):
    empty_personage.user = user_api_client.user
    empty_personage.save()
    response = user_api_client.post(f"/api/personages/{empty_personage.uuid}/generate/")
    empty_personage.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "uuid": f"{empty_personage.uuid}",
        "user": {
            "uuid": f"{empty_personage.user.uuid}",
            "username": empty_personage.user.username,
            "name": empty_personage.user.name,
            "url": f"http://testserver{empty_personage.user.get_absolute_url()}",
            "avatar": empty_personage.user.avatar.url,
        },
        "age": empty_personage.age,
        "gender": empty_personage.gender,
        "orientation": empty_personage.orientation,
        "disease": {
            "uuid": f"{empty_personage.disease.uuid}",
            "name": empty_personage.disease.name,
            "degree_percent": empty_personage.disease.degree_percent,
            "is_curable": empty_personage.disease.is_curable,
        },
        "profession": {
            "uuid": f"{empty_personage.profession.uuid}",
            "name": empty_personage.profession.name,
            "additional_skill": empty_personage.profession.additional_skill,
            "experience": f"{empty_personage.profession.experience}",
        },
        "phobia": {
            "uuid": f"{empty_personage.phobia.uuid}",
            "name": empty_personage.phobia.name,
            "stage": f"{empty_personage.phobia.stage}",
        },
        "hobby": {
            "uuid": f"{empty_personage.hobby.uuid}",
            "name": empty_personage.hobby.name,
            "experience": f"{empty_personage.hobby.experience}",
        },
        "character": {
            "uuid": f"{empty_personage.character.uuid}",
            "name": empty_personage.character.name,
        },
        "additional_info": {
            "uuid": f"{empty_personage.additional_info.uuid}",
            "name": empty_personage.additional_info.name,
        },
        "baggage": {
            "uuid": f"{empty_personage.baggage.uuid}",
            "name": empty_personage.baggage.name,
            "status": f"{empty_personage.baggage.status}",
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
            for action_card_usage in empty_personage.action_cards.all()
        ],
    }


def test_personage_generate_another_user(user_api_client, empty_personage):
    response = user_api_client.post(f"/api/personages/{empty_personage.uuid}/generate/")

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == {
        "detail": "You do not have permission to perform this action.",
    }
