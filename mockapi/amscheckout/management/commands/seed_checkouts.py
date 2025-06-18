import random
import requests
from django.core.management.base import BaseCommand
from faker import Faker
from amscheckout.models import Checkout

API_URL = "https://assets-service-production.up.railway.app/assets/"

class Command(BaseCommand):
    help = 'Seed 20 fake checkout/checkin records with correct exclusive fields and is_resolved flag'

    def handle(self, *args, **kwargs):
        fake = Faker()
        Checkout.objects.all().delete()

        # Fetch asset data
        resp = requests.get(API_URL)
        resp.raise_for_status()
        assets = resp.json()
        asset_choices = [(a["id"], a["name"]) for a in assets if a.get("name")]

        locations = ["Manila HQ", "Cebu Branch", "Makati Office", "Davao Hub", "QC Tech Center"]
        num_records = 20

        for _ in range(num_records):
            ticket_id = f"TK-{fake.unique.random_int(min=1000, max=9999)}"
            requestor = fake.name()
            requestor_location = random.choice(locations)

            if random.random() < 0.8:
                # Checkout (80%)
                asset_id, asset_name = random.choice(asset_choices)
                checkout_date = fake.date_between(start_date='-30d', end_date='today')
                return_date = fake.date_between(start_date=checkout_date, end_date='today') if random.random() < 0.3 else None

                Checkout.objects.create(
                    ticket_id=ticket_id,
                    asset_id=asset_id,
                    asset_name=asset_name,
                    requestor=requestor,
                    requestor_location=requestor_location,
                    checkout_date=checkout_date,
                    checkin_date=None,
                    return_date=return_date,
                    is_resolved=False,  # still unresolved when checked out
                    checkout_ref_id="1"
                )
            else:
                # Check-in (20%)
                checkin_date = fake.date_between(start_date='-30d', end_date='today')

                Checkout.objects.create(
                    ticket_id=ticket_id,
                    asset_id=None,
                    asset_name="",
                    requestor=requestor,
                    requestor_location=requestor_location,
                    checkout_date=None,
                    checkin_date=checkin_date,
                    return_date=None,
                    is_resolved=True,  # resolved upon check-in
                    checkout_ref_id="1"
                )

        self.stdout.write(self.style.SUCCESS(f'✅ Seeded {num_records} check-in/checkout records with correct field sets and is_resolved flag.'))
