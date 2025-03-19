from django import forms
from .models import JobListing, Application

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'salary', 'location']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = []
