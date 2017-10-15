# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count, Sum
from django.shortcuts import render

from products.models import Product


def index(request):
   context = {}
   primary_categories = Product.objects.values('primary_category').annotate(
       total=Count('id'),
       inventory=Sum('inventory'),
       inventory_value=Sum('inventory_price')).order_by('-total')
   secondary_categories = Product.objects.values('secondary_category').annotate(
       total=Count('id'),
       inventory=Sum('inventory'),
       inventory_value=Sum('inventory_price')).order_by('-total')

   context = {
       'primary_categories': primary_categories,
       'secondary_categories': secondary_categories,
   }
   return render(
       request,
       'products/index.html',
       context)
