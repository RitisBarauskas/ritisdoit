from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls'), name='articles'),
    path('users/', include('users.urls'), name='users'),
]
