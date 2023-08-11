from rest_framework import viewsets
from models import BroadcastingChannel
from serializers import BroadcastingChannelSerializer


class BroadcastingChannelViewSet(viewsets.ModelViewSet):
    queryset = BroadcastingChannel.objects.all()
    serializer_class = BroadcastingChannelSerializer
