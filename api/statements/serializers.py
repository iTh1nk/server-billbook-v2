from rest_framework import serializers

from api.models import Statements

from . import models


class StatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statements
        fields = "__all__"
