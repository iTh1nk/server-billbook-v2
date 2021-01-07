from rest_framework import serializers

from api.models import APNsToken


class ApnsTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = APNsToken
        fields = '__all__'