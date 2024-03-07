from django.shortcuts import render, get_object_or_404

from .models import Article, Category
from .enums import ArticleType


def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {'articles': articles, 'categories': categories}
    return render(request, 'articles/index.html', context)


def articles_of_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = category.articles.all()
    categories = Category.objects.all()
    context = {'articles': articles, 'categories': categories}
    return render(request, 'articles/index.html', context)


def long_reads(request):
    articles = Article.objects.filter(type=ArticleType.LONG_READ)
    categories = Category.objects.all()
    context = {'articles': articles, 'categories': categories}
    return render(request, 'articles/index.html', context)


def news(request):
    articles = Article.objects.filter(type=ArticleType.NEWS)
    categories = Category.objects.all()
    context = {'articles': articles, 'categories': categories}
    return render(request, 'articles/index.html', context)
