
from django.contrib import admin
from django.urls import path
from AppAssignment import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('image/', views.image),
    path('', views.home),
    path('contact/', views.contact),
    path('about/', views.about),
    path('gallery/', views.gallery),
    path('join/', views.join, name='join'),
    path('details/', views.details, name='details')





]
