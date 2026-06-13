from django.db import models


class Patient(models.Model):

    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    )

    patient_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    name = models.CharField(
        max_length=100
    )

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField()

    address = models.TextField()

    emergency_contact = models.CharField(
        max_length=15
    )

    registration_date = models.DateField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.patient_id:

            last_patient = Patient.objects.order_by(
                '-id'
            ).first()

            if last_patient:
                number = last_patient.id + 1
            else:
                number = 1

            self.patient_id = (
                f'PAT{number:04d}'
            )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):

        return (
            f'{self.patient_id} - {self.name}'
        )