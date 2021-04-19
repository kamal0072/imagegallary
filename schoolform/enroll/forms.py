from django import forms
from .models import CollageModel


class StudentForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField(widget=forms.Textarea)


