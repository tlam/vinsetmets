# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django import db
from django.conf import settings
from django.core.management.base import BaseCommand
import requests

from lcbo.models import Booze
from products.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):  # pragma: no cover
        added_on = datetime.now().date()
        url = 'https://lcboapi.com/products'
        headers = {
            'Authorization': 'Token {}'.format(settings.LCBO_API_KEY)
        }
        payload = {
            'page': 1,
            'per_page': 100,
            'where_not': 'is_dead,is_discontinued',
        }

        while True:
            response = requests.get(url, headers=headers, params=payload)
            if not response.ok:
                break

            output = response.json()
            pager = output['pager']
            print('Page {} / {}'.format(pager['current_page'], pager['total_pages']))
            for product in output['result']:
                if product['alcohol_content'] == 0:
                    continue
                obj, created = Product.objects.update_or_create(
                    id=product['id'],
                    defaults={
                        'name': product['name'].encode('utf-8'),
                        'origin': product['origin'],
                        'description': product['description'] or '',
                        'price': product['price_in_cents'] * 0.01,
                        'regular_price': product['regular_price_in_cents'] * 0.01,
                        'primary_category': product['primary_category'] or '',
                        'secondary_category': product['secondary_category'] or '',
                        'tertiary_category': product['tertiary_category'] or '',
                        'style': product['style'] or '',
                        'unit_volume': product['package_unit_volume_in_milliliters'],
                        'varietal': product['varietal'] or '',
                        'alcohol': product['alcohol_content'] * 0.01,
                        'sugar': product['sugar_content'] or '',
                        'sugar_in_grams': product['sugar_in_grams_per_liter'] or 0,
                        'producer': product['producer_name'] or '',
                        'stock_type': product['stock_type'] or '',
                        'tasting_notes': product['tasting_note'] or '',
                        'serving_suggestion': product['serving_suggestion'] or '',
                        'is_seasonal': product['is_seasonal'],
                        'is_vqa': product['is_vqa'],
                        'is_ocb': product['is_ocb'],
                        'image_url': product['image_url'] or '',
                        'image_thumb_url': product['image_thumb_url'] or '',
                        'has_limited_time_offer': product['has_limited_time_offer'],
                        'has_value_added_promotion': product['has_value_added_promotion'],
                        'inventory': product['inventory_count'] or 0,
                        'inventory_price': (product['inventory_price_in_cents'] or 0) * 0.01,
                        'inventory_volume': product['inventory_volume_in_milliliters'] or 0,
                        'limited_time_offer_ends': product['limited_time_offer_ends_on'] or '',
                        'limited_time_offer_savings': product['limited_time_offer_savings_in_cents'] * 0.01,
                        'released_on': product['released_on'] or '',
                        'tags': product['tags'].encode('utf-8'),
                        'total_package_units': product['total_package_units'],
                        'volume': product['volume_in_milliliters']
                    }
                )

                try:
                    obj, created = Booze.objects.update_or_create(
                        product_id=product['id'],
                        added_on=added_on,
                        defaults={
                            'name': product['name'].encode('utf-8'),
                            'origin': product['origin'],
                            'price': product['price_in_cents'] * 0.01,
                            'regular_price': product['regular_price_in_cents'] * 0.01,
                            'primary_category': product['primary_category'] or '',
                            'secondary_category': product['secondary_category'] or '',
                            'tertiary_category': product['tertiary_category'] or '',
                            'style': product['style'] or '',
                            'unit_volume': product['package_unit_volume_in_milliliters'],
                            'varietal': product['varietal'] or '',
                            'alcohol': product['alcohol_content'] * 0.01,
                            'sugar': product['sugar_content'] or '',
                            'sugar_in_grams': product['sugar_in_grams_per_liter'] or 0,
                            'producer': product['producer_name'] or '',
                            'stock_type': product['stock_type'] or '',
                            'tasting_notes': product['tasting_note'] or '',
                            'is_seasonal': product['is_seasonal'],
                            'is_vqa': product['is_vqa'],
                            'is_ocb': product['is_ocb'],
                            'has_limited_time_offer': product['has_limited_time_offer'],
                            'has_value_added_promotion': product['has_value_added_promotion'],
                            'inventory': product['inventory_count'] or 0,
                            'inventory_price': (product['inventory_price_in_cents'] or 0) * 0.01,
                            'inventory_volume': product['inventory_volume_in_milliliters'] or 0,
                            'limited_time_offer_ends': product['limited_time_offer_ends_on'] or '',
                            'limited_time_offer_savings': product['limited_time_offer_savings_in_cents'] * 0.01,
                            'released_on': product['released_on'] or '',
                            'total_package_units': product['total_package_units'],
                            'volume': product['volume_in_milliliters']
                        }
                    )
                except db.utils.IntegrityError:
                    pass

            payload['page'] = pager['next_page']
            if not payload['page']:
                break
            payload['page'] = pager['next_page']
            if not payload['page']:
                break
