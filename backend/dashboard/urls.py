from django.urls import path

from dashboard.views import (
    DashboardView,
    TestEmailView
)

urlpatterns = [

    path( '', DashboardView.as_view(), name='dashboard'),
    path( 'test-email/', TestEmailView.as_view(), name='test-email'),
]