from django.shortcuts import render 
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def newarrival(request): 
        products = product.objects.all()
        context = {'products': products } 
        return render(request,'newarrival.html',context=context)

def categories(request):
    if request.method == "GET":
        return render(request,"categories.html") 
def cart(request):
    
    items = orderItem.objects.all()
    context = {'items': items}
    return render(request,"cart.html",context=context) 