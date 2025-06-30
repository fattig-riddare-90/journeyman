from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import DiaryEntry
from .forms import DiaryEntryForm

# Create your views here.

@login_required
def public_entries(request):
    entries = DiaryEntry.objects.filter(is_public=True).exclude(user=request.user)
    return render(request, 'tracker/public_entries.html', {'entries': entries})

@login_required
def my_entries(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'tracker/my_entries.html', {'entries': entries})

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('my_entries')
    else:
        form = DiaryEntryForm()
    return render(request, 'tracker/create_entry.html', {'form': form})