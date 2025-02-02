from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MultiplicationResult
from .serializers import MultiplicationResultSerializer

@api_view(['POST'])
def multiply_numbers(request):
    if request.method == 'POST':
        # Get numbers from request data
        num1 = request.data.get('num1')
        num2 = request.data.get('num2')

        # Check if both numbers are provided
        if num1 is None or num2 is None:
            return Response({"error": "Both numbers are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Perform multiplication
        result = num1 * num2

        # Store multiplication result in the database
        multiplication_result = MultiplicationResult.objects.create(num1=num1, num2=num2, result=result)

        # Serialize the result for the response
        serializer = MultiplicationResultSerializer(multiplication_result)

        # Return the serialized data with a 201 status
        return Response(serializer.data, status=status.HTTP_201_CREATED)
