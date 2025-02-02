from django.db import models
from django.utils.timezone import now

# Create your models here.
class MultiplicationResult(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.IntegerField()
    created_at = models.DateTimeField(default=now)  # Store timestamp of creation

    def __str__(self):
        return f'{self.num1} * {self.num2} = {self.result} at {self.created_at}'