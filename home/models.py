from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE = ( 

    ('positive' , 'Positive'),
    ('negative' , 'Negative')
)

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    income = models.FloatField()
    balance = models.FloatField(blank= True , null= True)
    expenses = models.FloatField(default= 0)


class Expense(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length= 100)
    amount = models.FloatField(default=0, null= True)
    expense_type = models.CharField(max_length=  100, choices= TYPE)

    def __str__(self):
        return self.name

    
