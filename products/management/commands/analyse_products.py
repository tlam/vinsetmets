# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
import pandas as pd


class Command(BaseCommand):

    def handle(self, *args, **options):  # pragma: no cover
        df = pd.read_csv('/tmp/products.csv')
        results = df.sort_values(['inventory'], ascending=False)
        print(results[['name', 'inventory']].head(n=50))
