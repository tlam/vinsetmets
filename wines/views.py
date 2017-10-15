# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from wines.forms import WineForm
from wines.models import Wine


def index(request):
    wines = []
    form = WineForm(request.GET)
    if form.is_valid():
        fields = {}

        for field in ['style', 'colour', 'fruit', 'sweetness', 'tannin', 'body', 'acidity', 'alcohol']:
            value = form.cleaned_data[field]
            if value:
                fields[field] = value
        wines = Wine.objects.filter(**fields)

    context = {
        'form': form,
        'wines': wines,
    }
    return render(
        request,
        'wines/index.html',
        context)
