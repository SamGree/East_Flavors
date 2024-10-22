from django.urls import path
from . import views


urlpatterns = [
    # This will map the root URL to the home view
    path('', views.home_view, name='home'),
    path('menu', views.menu_view, name='menu'),
]

