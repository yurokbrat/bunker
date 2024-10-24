from rest_framework import serializers


class BuildInfoSerializer(serializers.Serializer):
    build_id = serializers.UUIDField()
    build_date = serializers.DateTimeField()
