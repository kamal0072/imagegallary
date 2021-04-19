
from django.contrib import admin
from django.urls import path
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.CollageListView.as_view(),name='home'),
    path('detail/<int:id>',views.CollageDetailView.as_view(),name='detail'),
]
