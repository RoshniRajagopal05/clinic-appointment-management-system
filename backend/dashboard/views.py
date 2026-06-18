from datetime import date

from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.permissions import IsAdmin

from patients.models import Patient

from doctors.models import (
    Doctor,
    DoctorAvailability
)

from appointments.models import Appointment
from django.core.mail import send_mail


class DashboardView(APIView):

    permission_classes = [
        IsAdmin
    ]

    def get(self, request):

        today = date.today()

        weekday = (
            today.strftime('%A')
            .upper()
        )

        upcoming_appointments = (
            Appointment.objects.filter(
                appointment_date__gte=today
            )
            .order_by(
                'appointment_date',
                'appointment_time'
            )[:5]
        )

        recent_patients = (
            Patient.objects.order_by(
                '-registration_date'
            )[:5]
        )

        doctor_availability = (
            DoctorAvailability.objects.filter(
                working_day=weekday
            )
        )

        data = {

            'total_patients':
            Patient.objects.count(),

            'total_doctors':
            Doctor.objects.count(),

            'today_appointments':
            Appointment.objects.filter(
                appointment_date=today
            ).count(),

            'completed_appointments':
            Appointment.objects.filter(
                status='COMPLETED'
            ).count(),

            'cancelled_appointments':
            Appointment.objects.filter(
                status='CANCELLED'
            ).count(),

            'no_shows':
            Appointment.objects.filter(
                status='NO_SHOW'
            ).count(),

            'upcoming_appointments': [

                {
                    'patient_name':
                    appointment.patient.name,

                    'doctor_name':
                    appointment.doctor.name,

                    'appointment_date':
                    appointment.appointment_date,

                    'appointment_time':
                    appointment.appointment_time
                }

                for appointment in upcoming_appointments
            ],

            'recent_registrations': [

                {
                    'patient_name':
                    patient.name,

                    'registration_date':
                    patient.registration_date
                }

                for patient in recent_patients
            ],

            'doctor_availability_today': [

                {
                    'doctor_name':
                    availability.doctor.name,

                    'working_day':
                    availability.working_day,

                    'start_time':
                    availability.start_time,

                    'end_time':
                    availability.end_time
                }

                for availability in doctor_availability
            ]
        }

        return Response(data)
    
class TestEmailView(APIView):

    permission_classes = [IsAdmin]

    def get(self, request):

        send_mail(
            subject='Clinic Appointment Test',
            message='Mailtrap is working successfully.',
            from_email='clinic@example.com',
            recipient_list=['test@example.com'],
            fail_silently=False
        )

        return Response({
            'message': 'Email sent successfully'
        })    