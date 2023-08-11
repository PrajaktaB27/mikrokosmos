from django.contrib import admin
from .models import BroadcastingChannel, Playlist, Track

admin.site.register(BroadcastingChannel)
admin.site.register(Playlist)
admin.site.register(Track)
