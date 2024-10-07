# api/management/commands/seed.py

from django.core.management.base import BaseCommand
from api.models import User, UserGroup

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Create Users
        user1 = User.objects.create(name='Alice', email='alice@example.com')
        user2 = User.objects.create(name='Bob', email='bob@example.com')
        user3 = User.objects.create(name='Charlie', email='charlie@example.com')

        # Create User Groups
        group1 = UserGroup.objects.create(name='Admins')
        group2 = UserGroup.objects.create(name='Editors')
        group3 = UserGroup.objects.create(name='Viewers')

        # Associate Users with Groups
        group1.users.add(user1, user2)
        group2.users.add(user2, user3)
        group3.users.add(user1, user3)

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
