from django import forms
from .models import Meeting, MeetingMinutes, Resource, Event


class ProductForm(forms.ModelForm):
    
    class Meta:
        model=Meeting
        fields = '__all__'

class ResourceForm(forms.ModelForm):
    
    class Meta:
        model=Resource
        fields = '__all__'