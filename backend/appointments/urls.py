from django.urls import path

from appointments.views import (
    AppointmentListCreateView,
    AppointmentDetailView
)

urlpatterns = [

    path('', AppointmentListCreateView.as_view(),name='appointments'),
    path('<int:pk>/',AppointmentDetailView.as_view(),name='appointment-detail'),
]