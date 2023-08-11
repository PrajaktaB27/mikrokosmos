from django.db import models
from django.contrib.auth.models import User


class BroadcastingChannel(models.Model):
    channel_name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(BroadcastingChannel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Track(models.Model):
    track_name = models.CharField(max_length=255)
    spotify_track_id = models.CharField(max_length=255, unique=True)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    duration_ms = models.PositiveIntegerField()
    preview_url = models.URLField()
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
