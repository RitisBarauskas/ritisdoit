from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_first.urls'), name='app_first'),
    path('app_second/', include('app_second.urls'), name='app_second'),
]
