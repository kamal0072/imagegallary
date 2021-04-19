
from django.contrib import admin
from django.urls import path
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.UserAddandShow.as_view(),name='UserAddandShow'),
    # path('',views.add_show,name='addandshow'),
    path('delete/<int:id>/',views.delete,name='deletedata'),
    path('<int:id>/',views.update,name='update'),
]
