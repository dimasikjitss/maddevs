from django.contrib import admin

from . import models


@admin.register(models.InstagramUser, models.PostInfo)
class InstagramModelAdmin(admin.ModelAdmin):
    pass