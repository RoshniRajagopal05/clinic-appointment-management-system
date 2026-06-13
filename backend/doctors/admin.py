from django.contrib import admin

from doctors.models import (
    Doctor,
    DoctorAvailability,
    DoctorLeave
)

admin.site.register(Doctor)

admin.site.register(
    DoctorAvailability
)

admin.site.register(
    DoctorLeave
)