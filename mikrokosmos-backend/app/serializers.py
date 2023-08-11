from rest_framework import serializers
from models import BroadcastingChannel


class BroadcastingChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BroadcastingChannel
        fields = '__all__'
