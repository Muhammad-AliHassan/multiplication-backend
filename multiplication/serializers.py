from rest_framework import serializers
from .models import MultiplicationResult

class MultiplicationResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiplicationResult
        fields = ['num1', 'num2', 'result', 'created_at']
