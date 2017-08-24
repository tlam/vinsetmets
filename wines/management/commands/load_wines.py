import csv

from django.core.management.base import BaseCommand

from aliases.models import Alias
from grapes.models import Grape
from wines.models import Style, Wine


class Command(BaseCommand):

    def handle(self, *args, **options):  # pragma: no cover
        csv_file = 'wines/fixtures/wines.csv'
        with open(csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                style, created = Style.objects.get_or_create(
                    name=row[1])

                wine, created = Wine.objects.get_or_create(
                    name=row[0],
                    defaults={
                        'style': style,
                        'label': row[2],
                        'origin': row[3],
                        'fruit': row[4],
                        'body': row[5],
                        'sweetness': row[6] or 0,
                        'acidity': row[7],
                        'alcohol': row[8],
                        'tannin': row[9] or 0
                    })

                for grape in row[10].split(','):
                    new_grape, created = Grape.objects.get_or_create(
                        name=grape)
                    wine.grapes.add(new_grape)

                for alias in row[11].split(','):
                    if not alias:
                        continue
                    new_alias, created = Alias.objects.get_or_create(
                        name=alias,
                        wine=wine)
