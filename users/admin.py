from django.contrib import admin

from . import models


@admin.register(models.User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["username", "id"]
