from django.db.models import Model
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView


class IsGameCreator(IsAuthenticated):
    def has_object_permission(self, request: Request, view: APIView, obj: Model):
        return obj.creator == request.user


class IsRelatedPersonage(IsAuthenticated):
    def has_object_permission(self, request: Request, view: APIView, obj: Model):
        return obj.user == request.user
