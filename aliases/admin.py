# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from aliases.models import Alias


class AliasAdmin(admin.ModelAdmin):
    pass


admin.site.register(Alias, AliasAdmin)
