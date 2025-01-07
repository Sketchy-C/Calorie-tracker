from django.shortcuts import render
from django.http import HttpResponse
from . models import Food
def index(request):
    foods = Food.objects.all()
    return render(request, 'index.html',{'foods':foods})
    