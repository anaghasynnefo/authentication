from django.db import models
class Employee(models.Model):
    employee_name=models.CharField(max_length=28)
    employee_password=models.CharField(max_length=28)
def __str__(self):
    return self.employee_name


# Create your models here.
