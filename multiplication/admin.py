# Register your models here.
from django.contrib import admin
from .models import MultiplicationResult

@admin.register(MultiplicationResult)
class MultiplicationResultAdmin(admin.ModelAdmin):
    list_display = ('num1', 'num2', 'result', 'created_at')