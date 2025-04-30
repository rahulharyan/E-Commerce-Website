from django.contrib import admin
from base.models import Products,cartModel
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['category','name','desc','price','p_images']

admin.site.register(Products,ProductAdmin)

admin.site.register(cartModel)