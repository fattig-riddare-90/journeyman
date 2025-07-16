from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from users.forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def custom_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('/')

def create_new_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')
        else:
            logger.error("Form errors: %s", form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/create_user.html', {'form': form})

def home(request):
    return render(request, 'users/start.html')