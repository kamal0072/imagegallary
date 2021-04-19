from django.shortcuts import render
from .forms import MyimageForm
from .models import MyImage


def home(request):
    if request.method=="POST":
        form=MyimageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()            
    form = MyimageForm()
    img=MyImage.objects.all()
    return render(request,'images/home.html',{'form':form,'img':img})