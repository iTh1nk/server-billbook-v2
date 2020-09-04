from rest_framework import serializers

from api.models import Activities

from api import models


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activities
        fields = "__all__"


class ActivitiesFKSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activities
        fields = ('id', 'date', 'amount', 'totalBalance', 'is_read', 'user')
