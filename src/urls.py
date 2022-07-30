from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

import api.views as views
from accounts.views import UserTokenObtainView, RegisterView

router = routers.DefaultRouter()
router.register(r'animes', views.AnimeViewSet)
router.register(r'animes-add', views.AddAnimeView)
router.register(r'plateformes', views.PlateformeViewSet)

urlpatterns = [
    path('', views.index, name="home"),
    path('', include(router.urls)),

    # API
    path('register/', RegisterView.as_view(), name='register_user'),
    # path('animes-add', views.AddAnimeView.as_view(), name='register_user'),
    path('token/', UserTokenObtainView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
