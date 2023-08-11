import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class BroadcastingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        """
        Called when a WebSocket connection is closed.
        """
        pass

    async def receive(self, text_data=None, bytes_data=None):
        """
        Called with a decoded WebSocket frame.
        """
        pass
