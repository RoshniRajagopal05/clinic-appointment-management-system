from django.urls import path

from doctors.views import (
    DoctorListCreateView,
    DoctorDetailView
)

urlpatterns = [

    path('',DoctorListCreateView.as_view(),name='doctors'),
    path('<int:pk>/',DoctorDetailView.as_view(),name='doctor-detail'),
]