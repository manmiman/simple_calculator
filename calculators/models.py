from django.db import models

class Equation(models.Model):

    encoding = models.CharField(max_length=255)
    equation = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.equation
