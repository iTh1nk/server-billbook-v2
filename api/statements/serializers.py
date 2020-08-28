from rest_framework import serializers

from api.models import Statements

from api import models


class StatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statements
        fields = "__all__"
        depth = 1