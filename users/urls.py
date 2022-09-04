from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )

from .views import users_view, home_view


urlpatterns = [
    path("", home_view, name="home"),
    path('register/', users_view, name='register_user'),

    path('login/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(),name='token_refresh'),


]