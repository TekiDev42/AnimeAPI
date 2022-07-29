from django.contrib import admin
from django.urls import path

import api.views as views

urlpatterns = [
    path('', views.index, name="home"),
    # path('plateforme/add/', views.ajouter_plateforme, name="ajouter_plateforme"),
    path('admin/', admin.site.urls)
]
