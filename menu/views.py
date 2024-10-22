from django.shortcuts import render
from .models import Menu


def home_view(request):
    return render(request, 'menu/home.html')


def menu_view(request):
    menu = Menu.objects.all()
    context = {
        'menu_list': menu
    }
    return render(request, 'menu/menu.html', context)
