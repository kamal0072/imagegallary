
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='panel/home.html'),name='home'),
    path('dashboard/',TemplateView.as_view(template_name='panel/dashboard.html'),
    name='dashboard'),
    path('login/',auth_views.LoginView.as_view(template_name='panel/login.html'),
    name='login'),
    path('logout/',auth_views.LoginView.as_view(template_name='panel/logout.html'),
    name='logout'),
    path('changepass/',auth_views.PasswordChangeView.as_view(template_name='panel/changepass.html'),
    name='changepass'),













]
