from django.urls import path
from . import views

urlpatterns = [
    # auth
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # bookings
    path('book-table/', views.book_table, name='book-table'),
    path('user-bookings/', views.user_bookings, name='user-bookings'),
    path('book-table/', views.book_table, name='book-table'),
    path('get-booking/<int:id>/', views.get_booking, name='get-booking'),
     path('update-booking/<int:id>/', views.update_booking, name='update-booking'),
    path(
        'cancel-booking/<int:id>/',
        views.cancel_booking,
        name='cancel-booking'),
    ]
