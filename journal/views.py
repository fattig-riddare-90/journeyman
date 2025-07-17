from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import DiaryEntry
from .forms import DiaryEntryForm
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.


@login_required
def public_entries(request):
    entries = (
        DiaryEntry.objects
        .filter(is_public=True)
        .exclude(user=request.user)
    )
    return render(request, 'journal/public_entries.html', {'entries': entries})


@login_required
def my_entries(request):
    entries = DiaryEntry.objects.filter(user=request.user)

    filter_value = request.GET.get('filter')
    if filter_value == 'public':
        entries = entries.filter(is_public=True)
    elif filter_value == 'private':
        entries = entries.filter(is_public=False)

    return render(request, 'journal/my_entries.html', {'entries': entries})


@login_required
def create_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, "New entry created successfully.")
            return redirect('my_entries')
    else:
        form = DiaryEntryForm()
    return render(request, 'journal/create_entry.html', {'form': form})


@login_required
def edit_entry(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Entry updated successfully.")
            return redirect('my_entries')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'journal/edit_entry.html', {'form': form})


@login_required
def delete_entry(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, "Entry deleted successfully.")
        return redirect('my_entries')
    return render(request, 'journal/confirm_delete.html', {'entry': entry})
