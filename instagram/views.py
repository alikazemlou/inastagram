from django.shortcuts import render
from .models import post



def index(request):
    return render(request,'instagram/main.html')