from django.shortcuts import render
from django.urls import reverse
from .models import food
# Create your views here.

def food_list(request):
    food_list = food.objects.all()
    context = {
        "foods" : food_list
    }
    return render(request,"foods/list.html",context)

def food_details(request , id):

    food_details = food.objects.get(id=id)
    context = {
        "foods" : food_details
    }
    return render(request,"foods/details.html",context)