from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('public/', views.public_entries, name='public_entries'),
    path('my/', views.my_entries, name='my_entries'),
    path('create_entry/', views.create_entry, name='create_entry'),
    path('edit/<int:pk>/', views.edit_entry, name='edit_entry'),
    path('delete/<int:pk>/', views.delete_entry, name='delete_entry'),
    path('logout/', views.custom_logout, name='logout'),
]