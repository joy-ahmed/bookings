from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.User)
class CustomAdmin(admin.ModelAdmin):
    """ Custom User Admin """
    list_display = ('username', 'gender', 'language', 'currency', 'superhost')
    list_filter = ('currency', 'language', 'superhost',)
