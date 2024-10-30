from rest_framework import serializers

from bunker_game.game.models.vote import Vote, Voting
from bunker_game.game.serializers.game_serializers import GameShortSerializer
from bunker_game.game.serializers.personage_serializers import PersonageShortSerializer


class VoteSerializer(serializers.ModelSerializer):
    voter = PersonageShortSerializer(label="Голосующий", read_only=True)
    target = PersonageShortSerializer(label="Кандидат", read_only=True)

    class Meta:
        model = Vote
        fields = ("uuid", "voter", "target", "created_at")


class VotingSerializer(serializers.ModelSerializer):
    game = GameShortSerializer(label="Игра", read_only=True)
    votes = VoteSerializer(label="Голоса", many=True, read_only=True)

    class Meta:
        model = Voting
        fields = ("uuid", "game", "votes", "is_active", "created_at")


class GiveVoiceSerializer(serializers.Serializer):
    target = serializers.UUIDField(label="Кандидат", write_only=True)


class ResultVotingSerializer(serializers.Serializer):
    vote_count = serializers.IntegerField(read_only=True)
    personage = PersonageShortSerializer(read_only=True)
