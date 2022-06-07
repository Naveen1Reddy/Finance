from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    if request.method == "POST":
        text = request.POST.get("text")
        amount = request.POST.get('amount')
        expense_type = request.POST.get("expense_type")

        expense = Expense(name = text , amount = amount , expense_type = expense_type)
        expense.save()


    profile = Profile.objects.filter(user = request.user).first()
    context = {"profile" : profile}

    return render(request , "home.html",context)