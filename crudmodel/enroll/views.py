from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView

class UserAddandShow(TemplateView):
    template_name='enroll/addandshow.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        fm=StudentRegistration()
        stud=User.objects.all()
        context={'stu':stud,'form':fm}
        return context
    
    def post(self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
        return HttpResponseRedirect('/')
    


def update(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else: 
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})


#this Is for delete
def delete(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
