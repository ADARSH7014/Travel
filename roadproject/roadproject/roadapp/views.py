from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.


def demo(request):
    obj=Place.objects.all()
    member = Team.objects.all()
    return render(request,"index.html",{"result":obj,'new':member})
def home(request):
    return render(request,"about.html")
def about(request):
    return HttpResponse("It is all about")
def contact(request):
    return render(request,'manu.html')
def detail(request):
    return HttpResponse("All the details are given there")
def thanks(request):
    return render(request,"thanks.html")