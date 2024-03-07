from django.urls import path

from .views import index, articles_of_category, long_reads, news

app_name = 'articles'

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', articles_of_category, name='category'),
    path('long-reads/', long_reads, name='long_reads'),
    path('news/', news, name='news'),
]
