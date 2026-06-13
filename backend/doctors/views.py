from django_filters.rest_framework import (
    DjangoFilterBackend
)

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from doctors.models import Doctor

from doctors.serializers.doctor_serializer import (
    DoctorSerializer
)

from accounts.permissions import (
    IsAdmin
)


class DoctorListCreateView(
    ListCreateAPIView
):

    permission_classes = [
        IsAdmin
    ]

    serializer_class = (
        DoctorSerializer
    )

    queryset = (
        Doctor.objects.all()
    )

    filter_backends = [
        DjangoFilterBackend
    ]

    filterset_fields = [
        'name',
        'specialization'
    ]


class DoctorDetailView(
    RetrieveUpdateDestroyAPIView
):

    permission_classes = [
        IsAdmin
    ]

    serializer_class = (
        DoctorSerializer
    )

    queryset = (
        Doctor.objects.all()
    )