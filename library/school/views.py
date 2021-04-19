from django.shortcuts import render
from .models import BookMode
from django.core.paginator import Paginator

def home(request):
    books=BookMode.objects.all().order_by('id')
    paginator=Paginator(books,3,orphans=1)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    return render(request,'school/home.html',{'page_obj':page_obj})