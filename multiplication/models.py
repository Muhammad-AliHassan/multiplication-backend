from django.db import models
from django.utils.timezone import now

# Model to store multiplication results
class MultiplicationResult(models.Model):
    num1 = models.IntegerField()  # First number in the multiplication
    num2 = models.IntegerField()  # Second number in the multiplication
    result = models.IntegerField()  # Result of the multiplication
    created_at = models.DateTimeField(default=now)  # Timestamp when the result is created

    # String representation of the multiplication result
    def __str__(self):
        return f'{self.num1} * {self.num2} = {self.result} at {self.created_at}'
