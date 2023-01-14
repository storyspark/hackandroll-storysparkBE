from . import views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('storyboard', StoryboardViewset, basename='storyboards')

urlpatterns = [
    re_path('', include(router.urls)),
]
