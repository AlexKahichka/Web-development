from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.http import HttpResponse
from django.shortcuts import render

def greet(request):
    your_name = "Alex"  # Вы можете изменить это на любое имя или получить его из параметров запроса
    return HttpResponse(f"Hello, {your_name}!")
