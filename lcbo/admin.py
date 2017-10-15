# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.contrib import admin

from lcbo.models import Booze


class BoozeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product_id',
        'origin',
        'price',
        'limited_time_offer_savings',
        'inventory',
        'primary_category',
        'secondary_category',
        'added_on_format',
    )
    list_filter = (
        'primary_category',
        'secondary_category',
        'is_ocb',
    )
    search_fields = ['name', 'product_id']

    def added_on_format(self, obj):
        return obj.added_on.strftime('%b %d, %Y')

admin.site.register(Booze, BoozeAdmin)
