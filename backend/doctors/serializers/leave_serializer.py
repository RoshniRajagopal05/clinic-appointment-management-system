from datetime import date

from rest_framework import serializers

from doctors.models import (
    DoctorLeave
)


class DoctorLeaveSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = DoctorLeave

        fields = '__all__'

    def validate_leave_date(
        self,
        value
    ):

        if value < date.today():

            raise serializers.ValidationError(
                "Leave date cannot be in the past."
            )

        return value