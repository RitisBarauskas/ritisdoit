import random
import striHfng
import factory
from factory.django import DjangoModelFactory

from .models import Category, Article
from .enums import ArticleStatus, ArticleType


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word', locale='ru_RU')
    description = factory.Faker('sentence', locale='ru_RU', nb_words=6)


class ArticleFactory(DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('sentence', nb_words=4, locale='ru_RU')
    content = factory.Faker('text', locale='ru_RU')
    categories = None
    author = None
    status = None
    type = None

    @classmethod
    def _create(cls, model_class, *args, author=None, categories=None, article_type=None, status=None, **kwargs):
        if author is None:
            raise ValueError('Author is required')

        kwargs['author'] = author

        if categories is None:
            raise ValueError('Categories is required')

        if article_type is None:
            kwargs['type'] = random.choice(ArticleType.choices())[0]

        if status is None:
            kwargs['status'] = random.choice(ArticleStatus.choices())[0]

        obj = super()._create(model_class, *args, **kwargs)
        obj.categories.set(categories)

        return obj
