from django.shortcuts import render
from django import forms
from datetime import datetime
from .models import User
from django.core import validators


today_date=datetime.now()

# Create your views here.


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["First_name","Last_name","Email","Organization","Contact"]

    


def index(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            Name=form.cleaned_data["First_name"]
            Surname=form.cleaned_data["Last_name"]
            email=form.cleaned_data["Email"]
            contact=form.cleaned_data["Contact"]
            organization=form.cleaned_data["Organization"]
            print(Name)
            print(Surname)
            print(email)
            print(contact)
            print(organization)
            print(today_date)
            reg=User(First_name=Name,Last_name=Surname,Email=email,Organization=organization, Contact=contact)
            reg.save()

            return render(request,"complete.html")
        else:
            return render(request,"index.html",{"form":form})
    return render(request,"index.html",{"form":UserForm()})

def completed(request):
    return render(request,"completed.html")