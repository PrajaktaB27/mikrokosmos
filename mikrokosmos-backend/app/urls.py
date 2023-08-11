from rest_framework import routers
from view import BroadcastingChannelViewSet
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'channels', BroadcastingChannelViewSet)

urlpatterns = [
                  # Other URL patterns
                  path('admin/', admin.site.urls),
              ] + router.urls
