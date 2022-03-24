from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Amenity, models.Facility, models.HouseRule, models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Spaces",
            {"fields": ("guests", "bedrooms", "beds", "baths")},
        ),
        (
            "More About the Space",
            {"fields": ("amenities", "facilities", "house_rules")},
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "bedrooms",
        "baths",
        "guests",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    search_fields = ["=city", "^host__username"]

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    ordering = (
        "name",
        "price",
        "bedrooms",
    )

    def count_amenities(self, obj):
        print(obj.amenities.count())
        return obj.amenities.count()

    def count_photos(self, obj):
        print(obj.photos.count())
        return obj.photos.count()

    count_amenities.short_description = "cnt_amenities"
