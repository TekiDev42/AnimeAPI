from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import api.views as views
from accounts.views import create_user

router = routers.DefaultRouter()
router.register(r'animes', views.AnimeViewSet)

"""
POST
username
password
Connection: keep-alive
Authorization: Bearer Token

REFRESH TOKEN
refresh : refresh-token

"""

urlpatterns = [
    path('', views.index, name="home"),
    path('', include(router.urls)),
    path('signin/', create_user, name="signin"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls)
]
