from django.contrib import admin

from . import models


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["product", "cart"]


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    # list_display = ["product", "cart"]
    pass
