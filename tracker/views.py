from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import DiaryEntry

# Create your views here.

@login_required
def public_entries(request):
    entries = DiaryEntry.objects.filter(is_public=True).exclude(user=request.user)
    return render(request, 'tracker/my_entries.html', {'entries': entries})

@login_required
def my_entries(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'tracker/my_entries.html', {'entries': entries})