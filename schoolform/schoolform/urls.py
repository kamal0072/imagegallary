
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.StudentView.as_view(),name='home'),
    path('thanku/',views.Thankstempalte.as_view(),name='thanku'),
    path('collg/',views.collageCreateview.as_view(),name='collg'),
    path('collgdeatil/<int:pk>',views.CollageDetail.as_view(),name='collgdeatil'),
    path('collgupdate/<int:pk>',views.CollageUpdateView.as_view(),name='collgupdate'),
]
