from rest_framework import serializers

from api.models import Activities

from . import models


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activities
        fields = "__all__"
