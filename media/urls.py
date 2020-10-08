from django.contrib import admin
from django.urls import path
from pictures import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('upload/', views.loadPicture, name='upload'),
]
