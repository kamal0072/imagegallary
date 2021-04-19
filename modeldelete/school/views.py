from django.shortcuts import render
from .models import Student 
from .forms import StudentForm
from django.views.generic import CreateView,UpdateView,DeleteView
from django.views.generic import TemplateView



class StudentUpdateView(UpdateView):
    model=Student
    form_class=StudentForm
    template_name='school/update.html'
    success_url='/thanksupdate/'

class ThanksUpdate(TemplateView):
    template_name='school/thank.html'

class StudentDeleteView(DeleteView):
    model=Student
    success_url='/create/'