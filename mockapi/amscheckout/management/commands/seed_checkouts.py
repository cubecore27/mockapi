import requests
from django.core.management.base import BaseCommand
from amscheckout.models import Checkout

API_URL = "https://assets-service-production.up.railway.app/assets/"

class Command(BaseCommand):
    help = 'Seed only the 4 predefined checkout/checkin records'

    def handle(self, *args, **kwargs):
        Checkout.objects.all().delete()

        # Seed specific default records
        default_records = [
            {
                "ticket_id": "TK-9537",
                "asset_id": 22,
                "asset_name": "iPad Pro",
                "requestor_id": 1,
                "requestor": "Kelly Barron",
                "requestor_location": "Pasig Office",
                "checkout_date": "2025-06-16",
                "return_date": "2025-08-16",
                "checkin_date": None,
                "checkout_ref_id": None,
                "condition": None,
                "is_resolved": False,
            },
            {
                "ticket_id": "TK-3590",
                "asset_id": 24,
                "asset_name": "LENOVO",
                "requestor_id": 2,
                "requestor": "Tammy Sawyer",
                "requestor_location": "Quezon City Office",
                "checkout_date": "2025-06-13",
                "return_date": "2028-06-16",
                "checkin_date": None,
                "checkout_ref_id": None,
                "condition": None,
                "is_resolved": False,
            },
            {
                "ticket_id": "TK-6188",
                "asset_id": 25,
                "asset_name": "Samsung",
                "requestor_id": 3,
                "requestor": "Denise Jimenez",
                "requestor_location": "Manila Office",
                "checkout_date": "2025-06-13",
                "return_date": "2027-06-16",
                "checkin_date": "2027-06-16",
                "checkout_ref_id": 1,
                "condition": 9,
                "is_resolved": False,
            },
            {
                "ticket_id": "TK-6018",
                "asset_id": 27,
                "asset_name": "Samsuung 12",
                "requestor_id": 3,
                "requestor": "Denise Jimenez",
                "requestor_location": "Makati Office",
                "checkout_date": "2025-06-10",
                "return_date": "2025-06-16",
                "checkin_date": "2025-06-18",
                "checkout_ref_id": 1,
                "condition": 6,
                "is_resolved": False,
            },
        ]

        for record in default_records:
            Checkout.objects.create(**record)

        self.stdout.write(self.style.SUCCESS(
            f'✅ Seeded {len(default_records)} predefined check-in/checkout records.'
        ))
