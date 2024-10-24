from typing import Any

from django.conf import settings
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from bunker_game.game.serializers.build_info_serializer import BuildInfoSerializer


class BuildInfoView(APIView):
    serializer_class = BuildInfoSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return Response(
            {"build_id": settings.BUILD_ID, "build_date": settings.BUILD_DATE},
        )
