
from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet  , UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('articles', ArticleViewSet, basename='articles')

router.register('users', UserViewSet , basename='users' )




urlpatterns = [
    path('api/', include(router.urls)),

]