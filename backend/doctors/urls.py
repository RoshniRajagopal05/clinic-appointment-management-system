from django.urls import path

from doctors.views import (
    DoctorListCreateView,
    DoctorDetailView,
    DoctorAvailabilityListCreateView,
    DoctorAvailabilityDetailView,
    DoctorLeaveListCreateView,
    DoctorLeaveDetailView
)

urlpatterns = [

    path('',DoctorListCreateView.as_view(),name='doctors'),
    path('<int:pk>/',DoctorDetailView.as_view(),name='doctor-detail'),
    path('availability/',DoctorAvailabilityListCreateView.as_view(),name='availability'),
    path('availability/<int:pk>/',DoctorAvailabilityDetailView.as_view(),name='availability-detail'),
    path('leave/',DoctorLeaveListCreateView.as_view(),name='leave'),
    path('leave/<int:pk>/',DoctorLeaveDetailView.as_view(),name='leave-detail'),
]