from django.urls import path
from . import views

urlpatterns = [
    path('multiply/', views.multiply_numbers, name='multiply_numbers'),

]
