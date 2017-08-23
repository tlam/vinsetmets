import csv

from django.core.management.base import BaseCommand

from aliases.models import Alias
from grapes.models import Grape
from wines.models import Style, Wine


class Command(BaseCommand):

    def handle(self, *args, **options):  # pragma: no cover
        csv_file = 'wines/fixtures/wines.csv'
        with open(csv_file, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            reader.next()  # Skip header
            for row in reader:
                style, created = Style.objects.get_or_create(
                    name=row[1])
