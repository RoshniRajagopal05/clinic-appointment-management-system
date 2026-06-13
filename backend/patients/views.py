from django.shortcuts import render

from django_filters.rest_framework import (
    DjangoFilterBackend
)

# Create your views here.
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from patients.models import Patient

from patients.serializers.patient_serializer import (
    PatientSerializer
)
from accounts.permissions import (
    IsAdminOrReceptionist
)
class PatientListCreateView(
    ListCreateAPIView
):

    permission_classes = [
        IsAdminOrReceptionist
    ]

    serializer_class = (
        PatientSerializer
    )

    queryset = (
        Patient.objects.all()
    )

    filter_backends = [
        DjangoFilterBackend
    ]

    filterset_fields = [
        'name',
        'phone',
        'email'
    ]


class PatientDetailView(
    RetrieveUpdateDestroyAPIView
):

    permission_classes = [
        IsAdminOrReceptionist
    ]

    serializer_class = (
        PatientSerializer
    )

    queryset = (
        Patient.objects.all()
    )