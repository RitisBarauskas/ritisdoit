from django.core.management.base import BaseCommand

from users.factories import UserFactory


class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, default=1, nargs='?', help='Number of users to create')

    def handle(self, *args, **options):
        count = options['count']
        UserFactory.create_batch(count)
        self.stdout.write(self.style.SUCCESS(f'{count} users created'))
