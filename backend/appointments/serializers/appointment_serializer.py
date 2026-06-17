from datetime import date

from rest_framework import serializers

from appointments.models import Appointment

from doctors.models import (
    DoctorAvailability,
    DoctorLeave
)


class AppointmentSerializer(
    serializers.ModelSerializer
    
):

    patient_name = serializers.CharField(
    source='patient.name',
    read_only=True
)

    doctor_name = serializers.CharField(
    source='doctor.name',
    read_only=True
)
    
    
    class Meta:

        model = Appointment

        fields = [
    'id',
    'appointment_date',
    'appointment_time',
    'reason',
    'status',
    'patient',
    'patient_name',
    'doctor',
    'doctor_name'
]

    def validate(self, data):

        doctor = data.get(
            'doctor'
        )

        appointment_date = data.get(
            'appointment_date'
        )

        appointment_time = data.get(
            'appointment_time'
        )

        # ----------------------------------
        # Future Date Validation
        # ----------------------------------

        if appointment_date < date.today():

            raise serializers.ValidationError(
                "Appointment must be a future date."
            )

        # ----------------------------------
        # Doctor Leave Validation
        # ----------------------------------

        leave_exists = (
            DoctorLeave.objects.filter(
                doctor=doctor,
                leave_date=appointment_date
            ).exists()
        )

        if leave_exists:

            raise serializers.ValidationError(
                "Doctor is on leave."
            )

        # ----------------------------------
        # Working Day Validation
        # ----------------------------------

        weekday = (
            appointment_date
            .strftime('%A')
            .upper()
        )

        availability = (
            DoctorAvailability.objects.filter(
                doctor=doctor,
                working_day=weekday
            ).first()
        )

        if not availability:

            raise serializers.ValidationError(
                "Doctor is not working on this day."
            )

        # ----------------------------------
        # Working Hours Validation
        # ----------------------------------

        if (
            appointment_time
            < availability.start_time
            or
            appointment_time
            > availability.end_time
        ):

            raise serializers.ValidationError(
                "Appointment time is outside working hours."
            )

        # ----------------------------------
        # Double Booking Validation
        # ----------------------------------

        appointment_exists = (
            Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).exists()
        )

        if appointment_exists:

            raise serializers.ValidationError(
                "Appointment slot already booked."
            )

        return data