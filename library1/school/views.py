from django.shortcuts import render
from .models import BookMode
# from django.core.paginator import Paginator
from django.views.generic.list import ListView

class BookListView(ListView):
    model=BookMode
    template_name='school/home.html'
    ordering=['id']
    paginated_by=3
    paginate_orphans=1
    # context_name='page_obj'

    # def get_context_data(self,*args, **kwargs):
    #     try:
    #         return super(BookListView,self).get_context_data(*args, **kwargs)
    #     except:
    #         self.kwargs['page']=1
    #         return super(BookListView,self).get_context_data(*args, **kwargs)
            