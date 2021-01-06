from rest_framework import serializers

from api.models import APNsToken


class ApnsTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = APNsToken
        fields = ('id', 'username', 'apnsToken', 'environment', 'ipAddr', 'createdAt', 'updatedAt')