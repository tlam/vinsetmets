# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from aliases.models import Alias
from wines.models import Style, Wine


class AliasInline(admin.TabularInline):
    model = Alias
    extra = 0


class StyleAdmin(admin.ModelAdmin):
    model = Style
    list_display = ['name', 'order']


class WineAdmin(admin.ModelAdmin):
    model = Wine
    filter_horizontal = ('grapes', 'grows_best',)
    inlines = [
        AliasInline
    ]
    list_display = ['name', 'colour', 'style']


admin.site.register(Style, StyleAdmin)
admin.site.register(Wine, WineAdmin)
