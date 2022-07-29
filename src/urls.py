from django.contrib import admin
from django.urls import path

import api.views as views
from accounts.views import create_user

urlpatterns = [
    path('', views.index, name="home"),
    path('accounts/add/', create_user, name="add_user"),
    path('admin/', admin.site.urls)
]
