from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "product_type", "price", 'image_tag']
    filter_horizontal = ("sizes",)
    # fields = ['image_tag']
    readonly_fields = ['image_tag']

@admin.register(models.ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ["size"]
