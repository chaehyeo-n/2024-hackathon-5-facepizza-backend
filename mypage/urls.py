from django.urls import path, include
from rest_framework import routers
from .views import MypageViewSet
from character.views import CharacterViewSet

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mypage'

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("mypage", MypageViewSet, basename="mypage")
default_router.register("characters", CharacterViewSet, basename="character")

urlpatterns = [
    path('', include(default_router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)