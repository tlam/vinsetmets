# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Count, Sum
from django.http import JsonResponse
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


def show(request, product_id):
    context = {
        'product': Product.objects.get(pk=product_id)
    }
    return render(
        request,
        'products/show.html',
        context)


def stats(request, product_id):
    product = Product.objects.get(pk=product_id)
    data = {
        'history': []
    }
    for history in product.history():
        data['history'].append({
            'added_on': history.added_on,
            'inventory': history.inventory,
            'price': history.price
        })
    return JsonResponse(data)
