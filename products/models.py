# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from lcbo.models import Booze


class Product(models.Model):
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    regular_price = models.DecimalField(max_digits=12, decimal_places=2)
    primary_category = models.CharField(max_length=255, blank=True, default='')
    secondary_category = models.CharField(max_length=255, blank=True, default='')
    tertiary_category = models.CharField(max_length=255, blank=True, default='')
    style = models.CharField(max_length=255, blank=True, default='')
    unit_volume = models.PositiveIntegerField()  # ml
    varietal = models.CharField(max_length=255, blank=True, default='')
    alcohol = models.PositiveIntegerField(default=0)
    sugar = models.CharField(max_length=255, blank=True, default='')  # Sugar content
    sugar_in_grams = models.PositiveIntegerField(default=0)  # sugar in grams per L
    producer = models.CharField(max_length=255, blank=True, default='')
    stock_type = models.CharField(max_length=100, blank=True, default='')
    tasting_notes = models.TextField(blank=True, default='')
    serving_suggestion = models.TextField(blank=True, default='')
    is_seasonal = models.BooleanField(default=False)
    is_vqa = models.BooleanField(default=False)
    is_ocb = models.BooleanField(default=False)  # Ontario craft beer
    image_url = models.CharField(max_length=255, blank=True, default='')
    image_thumb_url = models.CharField(max_length=255, blank=True, default='')
    has_limited_time_offer = models.BooleanField(default=False)
    has_value_added_promotion = models.BooleanField(default=False)
    inventory = models.PositiveIntegerField(default=0)
    inventory_price = models.DecimalField(max_digits=12, decimal_places=2)
    inventory_volume = models.PositiveIntegerField(default=0)  # ml
    limited_time_offer_ends = models.CharField(max_length=255, blank=True, default='')
    limited_time_offer_savings = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='savings')
    released_on = models.CharField(max_length=255, blank=True, default='')
    tags = models.TextField(blank=True, default='')
    total_package_units = models.PositiveSmallIntegerField()
    volume = models.PositiveIntegerField(default=0)  # ml
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:show', args=[self.id])

    def history(self):
        return Booze.objects.filter(product_id=self.id)
