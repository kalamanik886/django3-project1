from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import RegisterModel
from django.contrib import messages

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, "home.html", {})

def register(request,*args, **kwargs):
    my_form = RegisterForm()
    if request.method == "POST":
        my_form = RegisterForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            RegisterModel.objects.create(**my_form.cleaned_data)
            my_form = RegisterForm()
            return redirect('end/')
        else:
            print(my_form.errors)
    context = {
        "form" : my_form
    }

    return render(request, "register.html", context)

def end(request, *args, **kwargs):
    return render(request, "end.html", {})
