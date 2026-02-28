from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
]