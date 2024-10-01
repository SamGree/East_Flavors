from django.shortcuts import render

def menu_view(request):
    return render(request, 'base.html')  # Renders the home.html template
