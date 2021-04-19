from django.shortcuts import render
from .forms import StudentForm
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import CollageModel
from django.views.generic import UpdateView

class collageCreateview(CreateView):
    model=CollageModel
    fields=['name','address','since']
    success_url='/thanku/'
    template_name='enroll/collage.html'

class CollageUpdateView(UpdateView):
    model=CollageModel
    fields=['name','address','since']
    success_url='/thanku/'

 


class CollageDetail(DetailView):
    model=CollageModel




class StudentView(FormView):
    form_class=StudentForm
    initial={'name':'i.e:Sonam','email':'i.e:abc@gmail.com','address':'i.e:delhi'}
    template_name='enroll/studentform.html'
    success_url='/thanku/'
    def form_valid(self, form):
        print("This Form Data:--",form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['address'])
        return HttpResponse("form Submitted")



class Thankstempalte(TemplateView):
    template_name='enroll/thanks.html'
