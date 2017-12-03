# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

from cuisines.models import Cuisine


def json_data(request):
    output = {
        'cuisines': []
    }
    cuisines = Cuisine.objects.all()
    for cuisine in cuisines:
        foods = []
        for food in cuisine.foods.all():
            foods.append({
                'name': food.name,
                'description': food.description,
                'image': food.image
            })
        output['cuisines'].append({
            'id': cuisine.id,
            'name': cuisine.name,
            'origin': cuisine.origin,
            'foods': foods
        })
    response = JsonResponse(output)
    return response
