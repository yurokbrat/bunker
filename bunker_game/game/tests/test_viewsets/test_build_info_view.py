from django.conf import settings
from rest_framework import status


def test_build_info_view(user_api_client):
    response = user_api_client.get("/api/build-info/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "build_id": settings.BUILD_ID,
        "build_date": settings.BUILD_DATE,
    }
