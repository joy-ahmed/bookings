from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomAdmin(UserAdmin):
    """ Custom User Admin """
    # list_display = ('username', 'gender', 'language', 'currency', 'superhost')
    # list_filter = ('currency', 'language', 'superhost',)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile", {
                "fields": ("avatar", "gender", "bio", "birthdate", "language", "currency", "superhost")
            }
        ),
    )
