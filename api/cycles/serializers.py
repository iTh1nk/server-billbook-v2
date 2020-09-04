from rest_framework import serializers

from api.models import Cycles

from api import models


class CyclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cycles
        fields = ('id', 'date', 'is_read', 'createdAt', 'updatedAt')


class CyclesFKSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cycles
        fields = ('id', 'date', 'is_read', 'createdAt', 'updatedAt', 'cycle_statements')
        depth = 1


class CyclesIsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cycles
        fields = ('id', 'is_read')

# class CyclesListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Cycles
#         fields = ('id', 'date', 'createdAt', 'updatedAt', 'cycle_statements')
#         depth = 1


# class CyclesListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Cycles
#         fields = ('id', 'date', 'createdAt', 'updatedAt', 'cycle_statements')
#         depth = 1
