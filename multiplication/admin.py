# Register your models here.
from django.contrib import admin
from .models import MultiplicationResult

# Admin configuration for the MultiplicationResult model
@admin.register(MultiplicationResult)
class MultiplicationResultAdmin(admin.ModelAdmin):
    # Display these fields in the list view in the admin panel
    list_display = ('num1', 'num2', 'result', 'created_at')
