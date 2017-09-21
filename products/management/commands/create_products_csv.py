# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv

from django.core.management.base import BaseCommand

from products.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):  # pragma: no cover
        header = [
            'name',
            'origin',
            'price',
            'primary_category',
            'secondary_category',
            'tertiary_category',
            'style',
            'unit_volume',
            'varietal',
            'stock_type',
            'inventory',
            'inventory_price',
            'inventory_volume',
        ]
        with open('/tmp/products.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            for product in Product.objects.all():
                row = []
                for attribute in header:
                    value = getattr(product, attribute)
                    if isinstance(value, basestring):
                        row.append(value.encode('utf-8'))
                    else:
                        row.append(value)
                writer.writerow(row)
