from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('category/<int:id>/', views.category, name='category'),
    path('about/<int:id>/', views.about, name='about'),
    path('Airways/<int:id>/', views.airways, name='Airways'),
    path('contact/', views.contact, name='contact'),
]