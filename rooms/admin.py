from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Defination """
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Defination """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")}
        ),
        (
            "Spaces",
            {"fields": ("guest", "beds", "bedrooms", "baths")}
        ),
        (
            "More About the Spaces",
            {"fields": ("amenities", "facilities", "house_rules")}

        ),
        (
            "Last Details",
            {"fields": ("host",)}

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
        "guest",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = ("instant_book", "room_type",
                   "amenities", "facilities", "house_rules", "city", "country",)

    search_fields = ("^city", "^host__username")
    filter_horizontal = ("amenities", "facilities", "house_rules")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Defination """
    pass
