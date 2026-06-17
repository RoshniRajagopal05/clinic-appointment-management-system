from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from appointments.models import (
    Appointment
)

from appointments.serializers.appointment_serializer import (
    AppointmentSerializer
)

from accounts.permissions import (
    IsAdminOrReceptionist
)

from django_filters.rest_framework import (
    DjangoFilterBackend
)

class AppointmentListCreateView(
    ListCreateAPIView
):

    permission_classes = [
        IsAdminOrReceptionist
    ]

    serializer_class = (
        AppointmentSerializer
    )

    queryset = (
        Appointment.objects.all()
    )

    filter_backends = [
        DjangoFilterBackend
    ]

    filterset_fields = [
        'doctor',
        'status',
        'appointment_date'
    ]

class AppointmentDetailView(
    RetrieveUpdateDestroyAPIView
):

    permission_classes = [
        IsAdminOrReceptionist
    ]

    serializer_class = (
        AppointmentSerializer
    )

    queryset = (
        Appointment.objects.all()
    )