# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from lcbo.models import Booze


class BoozeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product_id',
        'origin',
        'price',
        'inventory',
        'primary_category',
        'secondary_category',
        'added_on',
    )
    list_filter = (
        'primary_category',
        'secondary_category',
        'is_ocb',
    )
    search_fields = ['name', 'product_id']

admin.site.register(Booze, BoozeAdmin)
