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