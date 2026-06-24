from django.core.management.base import BaseCommand
from reservations.models import Table

class Command(BaseCommand):
    help = 'Seeds the database with the restaurant tables'

    def handle(self, *args, **kwargs):

        if Table.objects.exists():
            self.stdout.write(self.style.WARNING(
                'Tables already exist. Skipping seed to avoid duplicates.'
            ))
            return

        tables = [
            # Indoor
            { 'name': 'T1', 'section': 'indoor', 'capacity': 2 },
            { 'name': 'T2', 'section': 'indoor', 'capacity': 2 },
            { 'name': 'T3', 'section': 'indoor', 'capacity': 6 },
            { 'name': 'T4', 'section': 'indoor', 'capacity': 2 },
            { 'name': 'T5', 'section': 'indoor', 'capacity': 4 },
            # Patio 4-tops
            { 'name': 'SP1', 'section': 'patio', 'capacity': 2 },
            { 'name': 'SP2', 'section': 'patio', 'capacity': 2 },
            { 'name': 'SP3', 'section': 'patio', 'capacity': 2 },
            # Patio 2-tops
            { 'name': 'SP4', 'section': 'patio', 'capacity': 4 },
            { 'name': 'SP5', 'section': 'patio', 'capacity': 4 },
            { 'name': 'SP6', 'section': 'patio', 'capacity': 4 },
        ]

        for t in tables:
            Table.objects.create(
                name=t['name'],
                section=t['section'],
                capacity=t['capacity'],
                is_available=True
            )
            self.stdout.write(self.style.SUCCESS(f"Created table {t['name']}"))

        self.stdout.write(self.style.SUCCESS(
            f'\nDone. {len(tables)} tables added.'
        ))