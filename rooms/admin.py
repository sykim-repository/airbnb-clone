from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Amenity, models.Facility, models.HouseRule, models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass
