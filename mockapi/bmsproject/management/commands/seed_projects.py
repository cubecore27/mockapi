# bmsproject/management/commands/seed_projects.py

from django.core.management.base import BaseCommand
from faker import Faker
import random

from bmsproject.models import Project  # replace 'your_app' with the correct app name

fake = Faker()

def generate_items():
    items = []
    for _ in range(random.randint(3, 5)):
        items.append({
            "cost_element": f"CE-{random.randint(1000, 9999)}",
            "description": fake.sentence(),
            "estimated_cost": str(random.randint(100, 10000)),
            "account": random.randint(1, 5),
            "notes": fake.sentence()
        })
    return items

class Command(BaseCommand):
    help = 'Seed the database with sample Project data'

    def handle(self, *args, **kwargs):
        Project.objects.all().delete()
        for _ in range(20):
            Project.objects.create(
                title=fake.bs().title(),
                project_summary=fake.text(max_nb_chars=100),
                project_description=fake.paragraph(nb_sentences=5),
                performance_notes=fake.sentence(),
                department=random.randint(1, 5),
                fiscal_year=random.randint(1, 5),
                submitted_by_name=fake.name(),
                status=random.choice(['SUBMITTED', 'APPROVED', 'REJECTED']),
                performance_start_date=fake.date_between(start_date='-1y', end_date='today'),
                performance_end_date=fake.date_between(start_date='today', end_date='+1y'),
                external_system_id=f"EXT-{fake.unique.random_number(digits=5)}",
                items=generate_items()
            )
        self.stdout.write(self.style.SUCCESS("✔ Successfully seeded 20 Projects with nested items."))
