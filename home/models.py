from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE = ( 

    ('positive' , 'Positive'),
    ('negative' , 'Negative')
)

class profile(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    income = models.FloatField()
    balance = models.FloatField(null= True)


class Expense(models.Model):
    name = models.CharField(max_length= 100)
    expense_type = models.CharField(max_length=  100, choices= TYPE)

    def __str__(self):
        return self.name

    
