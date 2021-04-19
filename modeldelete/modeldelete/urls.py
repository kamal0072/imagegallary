
from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studelet/<int:pk>',views.StudentUpdateView.as_view(),name='home'),
]
