from django.urls import path
from . import views

# Define URL patterns for the app
urlpatterns = [
    # URL pattern for the multiply_numbers view
    path('multiply/', views.multiply_numbers, name='multiply_numbers'),
]
