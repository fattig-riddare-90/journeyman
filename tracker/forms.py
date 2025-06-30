from django import forms
from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['title', 'date', 'content', 'is_public']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }