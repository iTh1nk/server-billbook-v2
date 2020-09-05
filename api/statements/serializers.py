from rest_framework import serializers

from api.models import Statements

from api import models


class StatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statements
        fields = "__all__"


class StatementsFKSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statements
        fields = ('id', 'balance', 'notes', 'user', 'cycle', 'username', 'createdAt', 'updatedAt')
