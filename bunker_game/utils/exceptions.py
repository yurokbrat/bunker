from rest_framework import status
from rest_framework.exceptions import APIException


class GameStoppedError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Игра уже завершена"
    default_code = "game_stopped"


class GameActiveError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Игра уже активна"
    default_code = "game_is_active"


class VotingStoppedError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Голосование уже завершено"
    default_code = "voting_stopped"


class VotingActiveError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Голосование уже активно"
    default_code = "voting_is_active"


class AlreadyVotedError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Вы уже проголосовали"
    default_code = "already_voted"


class InvalidCharacteristicError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Характеристика не найдена"
    default_code = "invalid_characteristic"


class AlreadyUsedActionCardError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Карта действия уже использовалась"
    default_code = "already_used_action_card"


class NoVotesError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Нет голосов для голосования"
    default_code = "no_votes"


class NoPersonagesError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "В игре нет персонажей"
    default_code = "no_personages"


class NoDefaultCharacteristicError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Не найдены стандартные характеристики"
    default_code = "no_default_characteristic"


class UserNotCreatorGameError(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Вы не являетесь создателем игры"
    default_code = "user_not_creator_game"
