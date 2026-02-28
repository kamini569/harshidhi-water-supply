from django.shortcuts import render, redirect
from .models import Order

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        Order.objects.create(name=name, address=address, quantity=quantity)
        return redirect('home')
    return render(request, 'order.html')

def contact(request):
    return render(request, 'contact.html')