

# Create your models here.
from django.db import models


class Doctor(models.Model):

    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive')
    )

    doctor_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    name = models.CharField(
        max_length=100
    )

    specialization = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField()

    qualification = models.CharField(
        max_length=200
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    joining_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ACTIVE'
    )

    def save(self, *args, **kwargs):

        if not self.doctor_id:

            last_doctor = Doctor.objects.order_by(
                '-id'
            ).first()

            if last_doctor:
                number = last_doctor.id + 1
            else:
                number = 1

            self.doctor_id = (
                f'DOC{number:04d}'
            )

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):

        return (
            f'{self.doctor_id} - {self.name}'
        )