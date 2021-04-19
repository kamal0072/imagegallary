from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','password']
        widgets={'name':forms.TextInput(attrs={'class':'css1'}),
        'password':forms.PasswordInput(render_value=True,attrs={'class':'css2'})}