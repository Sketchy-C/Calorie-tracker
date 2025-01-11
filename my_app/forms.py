from django import forms
from .models import Food

class addFood(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['title','calories']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'bg-slate-100 border-slate-400 p-2 m-2'
            }),
            'calories': forms.TextInput(attrs={
                'class':'bg-slate-100 border-slate-400 p-2 m-2'
            }),
        }