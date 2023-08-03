from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import IntegerField
from django.db.models import Sum
# Create your models here.

class User(AbstractUser):
    is_admin=models.BooleanField('Is admin', default=False)
    is_employee=models.BooleanField('Is employee', default=False)
    Age=models.IntegerField(null=True,blank=True)
    Address=models.CharField(max_length=200,null=True,blank=True)
    Salary=models.IntegerField(null=True,blank=True)


class Sale(models.Model):
    employee=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    sale=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.employee.username

 
class AddBonus(models.Model):
    employee=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    Bonus=models.FloatField()
    date=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.employee.username
    

