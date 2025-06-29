from django.urls import path
from . import views

urlpatterns = [
    path('public/', views.public_entries, name='public_entries'),
    path('my/', views.my_entries, name='my_entries'),
]