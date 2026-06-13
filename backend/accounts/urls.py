from django.urls import path

from accounts.views import (
    CurrentUserView,
    ReceptionistListCreateView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('me/',CurrentUserView.as_view(),name='current-user'),
    path('receptionists/',ReceptionistListCreateView.as_view(),name='receptionists'),
]