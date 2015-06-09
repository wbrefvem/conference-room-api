from django.conf.urls import url, include
from rest_framework import routers
from rooms.api import views


router = routers.DefaultRouter()
router.register(r'buildings', views.BuildingViewSet)
router.register(r'rooms', views.RoomViewSet)

urlpatterns = [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
