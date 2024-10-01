from django.shortcuts import render

def menu_view(request):
    return render(request, 'home.html')  # Renders the home.html template
