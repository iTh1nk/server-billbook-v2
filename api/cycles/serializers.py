from rest_framework import serializers

from api.models import Cycles

from api import models


class CyclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cycles
        fields = "__all__"
