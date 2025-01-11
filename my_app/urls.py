from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addfood/',views.addfood,name='addfood'),
    path('delete/<int:food_id>/',views.delete_food,name ='delete_food')
    
]
