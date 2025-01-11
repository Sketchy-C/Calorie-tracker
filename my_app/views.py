from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from . models import Food
from .forms import addFood
from django.contrib import messages

def index(request):
    foods = Food.objects.all()
    total_cal = sum(food.calories for food in foods)

    return render(request, 'index.html',{'foods':foods, 'total_cal':total_cal})

def addfood(request):
    if request.method == 'POST':
        form = addFood(request.POST)
        if form.is_valid():
            food = form.save()
            messages.success(request,'Food post created successfully!')
            return redirect('index')
    else:
        form = addFood()
    return render(request, 'form.html',{
        'form': form,
    })

def delete_food(request, food_id):
    food = get_object_or_404(Food,id=food_id)
    food.delete()
    return redirect('index')