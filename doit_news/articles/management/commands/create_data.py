import random
import datetime

from django.core.management.base import BaseCommand

from articles.factories import CategoryFactory, ArticleFactory
from users.factories import UserFactory
from users.models import DoitUser
from articles.models import Category


class Command(BaseCommand):
    help = 'Create data'

    def add_arguments(self, parser):
        parser.add_argument('users', type=int, default=1, nargs='?', help='Number of users to create')
        parser.add_argument('categories', type=int, default=1, nargs='?', help='Number of categories to create')
        parser.add_argument('articles', type=int, default=1, nargs='?', help='Number of articles to create')

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS('Creating data...'))
        start = datetime.datetime.now()
        self.stdout.write(self.style.SUCCESS(f'Start time: {start}'))

        users_count = options['users']
        UserFactory.create_batch(users_count)
        self.stdout.write(self.style.SUCCESS(f'{users_count} users created'))

        categories_count = options['categories']
        CategoryFactory.create_batch(categories_count)
        self.stdout.write(self.style.SUCCESS(f'{categories_count} categories created'))

        articles_count = options['articles']

        users = DoitUser.objects.all()
        categories = list(Category.objects.all())

        for user in users:
            categories_of_articles = random.choices(categories, k=random.randint(1, 3))

            ArticleFactory.create_batch(articles_count, author=user, categories=categories_of_articles)
            self.stdout.write(self.style.SUCCESS(f'{articles_count} articles created'))

        end = datetime.datetime.now()
        self.stdout.write(self.style.SUCCESS(f'End time: {end}'))
        self.stdout.write(self.style.SUCCESS(f'Elapsed time: {end - start}'))

        self.stdout.write(self.style.SUCCESS(
            f'Total {users_count} users, '
            f'{categories_count} categories, '
            f'{articles_count * users_count} articles created'
        ))
        self.stdout.write(self.style.SUCCESS('Data created'))