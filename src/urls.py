from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import UserTokenObtainView, RegisterView

from api.api_views.anime.BaseGetView import AnimeGetView
from api.api_views.anime.BaseRetrieveView import AnimeRetrieveView
from api.api_views.plateforme.PlateformeViewSet import PlateformeViewSet

from api.views import index

urlpatterns = [
    path('', index, name="home"),

    # API
    path('anime/<int:pk>/', AnimeGetView.as_view(), name="get_anime"),
    path('animes/', AnimeRetrieveView.as_view(), name="all_animes"),

    path('plateformes/', PlateformeViewSet.as_view({'get': 'list'}), name="plateformes"),

    path('register/', RegisterView.as_view(), name='register_user'),
    path('token/', UserTokenObtainView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
