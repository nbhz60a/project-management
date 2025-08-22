from django import forms
from .models import Reminder, Project

class CompletedWorkForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['completed_work']

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['message', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
