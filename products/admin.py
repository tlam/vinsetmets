# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'origin',
        'price',
        'limited_time_offer_savings',
        'inventory',
        'primary_category',
        'style',
        'varietal',
    )
    list_filter = (
        'primary_category',
        'secondary_category',
        'has_limited_time_offer',
        'is_ocb',
    )
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
