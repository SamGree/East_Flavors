from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),  # This will map the root URL to the home view
]
