# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'origin',
        'price',
        'inventory',
        'primary_category',
        'secondary_category',
        'style',
        'varietal',
    )
    list_filter = (
        'primary_category',
        'secondary_category',
        'is_ocb',
    )
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
