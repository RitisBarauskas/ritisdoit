from enum import Enum


class ArticleType(Enum):
    NEWS = 'Новость'
    LONG_READ = 'Лонгрид'
    INTERVIEW = 'Интервью'

    def __str__(self):
        return self.name

    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]


class ArticleStatus(Enum):
    DRAFT = 'Черновик'
    PUBLISHED = 'Опубликовано'
    ARCHIVED = 'В архиве'

    def __str__(self):
        return self.name

    @classmethod
    def choices(cls):
        return [(tag.name, tag.value) for tag in cls]
