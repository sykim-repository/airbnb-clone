from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """REservation Admin Definition"""

    pass
