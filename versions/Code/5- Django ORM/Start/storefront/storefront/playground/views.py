from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def calculate():
    x= 69
    return x

def say_hello(request):
    x= calculate()
    y=69
    return render(request,'hello.html',{ 'name': 'Rahat'})
