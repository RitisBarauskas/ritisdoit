from django.shortcuts import render


def index(request):
    return render(request, 'app_first/index.html')


def about(request):
    return render(request, 'app_first/about.html')
