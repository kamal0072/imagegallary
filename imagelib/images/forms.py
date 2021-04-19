from django import forms
from .models import MyImage

class MyimageForm(forms.ModelForm):
    class Meta:
        model=MyImage
        fields='__all__'
        labels={'first_name':'First Name:','photo':'Person Photo'}