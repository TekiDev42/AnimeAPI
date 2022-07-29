from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import api.views as views
from accounts.views import create_user

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'animes', views.AnimeViewSet)

urlpatterns = [
    path('', views.index, name="home"),
    path('api/', include(router.urls)),
    path('accounts/add/', create_user, name="add_user"),
    path('admin/', admin.site.urls)
]
