from rest_framework import serializers

from doctors.models import (
    DoctorAvailability
)


class DoctorAvailabilitySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = DoctorAvailability

        fields = '__all__'

    def validate(self, data):

        start_time = data.get(
            'start_time'
        )

        end_time = data.get(
            'end_time'
        )

        if start_time >= end_time:

            raise serializers.ValidationError(
                "Start time must be before end time."
            )

        return data