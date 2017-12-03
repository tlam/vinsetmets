# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from cuisines.models import Cuisine, Food


class FoodInline(admin.TabularInline):
    model = Food
    extra = 0


class CuisineAdmin(admin.ModelAdmin):
    inlines = [
        FoodInline,
    ]


class FoodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Food, FoodAdmin)
