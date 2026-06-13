from django_filters.rest_framework import (
    DjangoFilterBackend
)

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from doctors.models import Doctor

from doctors.models import (
    DoctorAvailability,
    DoctorLeave
)

from doctors.serializers.availability_serializer import (
    DoctorAvailabilitySerializer
)

from doctors.serializers.leave_serializer import (
    DoctorLeaveSerializer
)

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
    
    
    from doctors.models import (
    DoctorAvailability,
    DoctorLeave
)



class DoctorAvailabilityListCreateView(
    ListCreateAPIView
):

    permission_classes = [
        IsAdmin
    ]

    serializer_class = (
        DoctorAvailabilitySerializer
    )

    queryset = (
        DoctorAvailability.objects.all()
    )
    
    
class DoctorAvailabilityDetailView(
    RetrieveUpdateDestroyAPIView
):

    permission_classes = [
        IsAdmin
    ]

    serializer_class = (
        DoctorAvailabilitySerializer
    )

    queryset = (
        DoctorAvailability.objects.all()
    )
    
    
class DoctorLeaveListCreateView(
    ListCreateAPIView
):

    permission_classes = [
        IsAdmin
    ]

    serializer_class = (
        DoctorLeaveSerializer
    )

    queryset = (
        DoctorLeave.objects.all()
    )        


class DoctorLeaveDetailView(
    RetrieveUpdateDestroyAPIView
):

    permission_classes = [
        IsAdmin
    ]

    serializer_class = (
        DoctorLeaveSerializer
    )

    queryset = (
        DoctorLeave.objects.all()
    )