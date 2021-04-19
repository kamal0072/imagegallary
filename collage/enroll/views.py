from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import CollageModel


class CollageDetailView(DetailView):
    model=CollageModel
    template_name='enroll/detail.html'
    context_object_name='collg'
    pk_url_kwarg='id'
  


class CollageListView(ListView):
    model=CollageModel
    template_name='enroll/home.html'
    context_object_name='mymodel'


    # def get_queryset(self):
    #     return CollageModel.objects.filter(name='iim')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["model"] =CollageModel.objects.all().order_by('name') 
    #     return context
    
    # def get_template_name(self):
    #     if self.request.COOKIES['user']=='kamal':
    #         template_name='enroll/kamal.html'
        
    #     else:
    #         template_name=self.template_name
    #         return [template_name]
