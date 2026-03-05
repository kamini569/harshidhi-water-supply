from django.shortcuts import render, redirect
from .models import Order, Contact


def home(request):
    return render(request, "home.html")


def services(request):
    return render(request, "services.html")


def pricing(request):
    return render(request, "pricing.html")


def order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        service = request.POST.get("service")
        qty = request.POST.get("qty")

        Order.objects.create(
            name=name,
            mobile=mobile,
            address=address,
            service=service,
            quantity=qty
        )

        return redirect("home")

    return render(request, "order.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")

        # Save data in database
        Contact.objects.create(
            name=name,
            mobile=mobile,
            message=message
        )

        return redirect('home')   

    return render(request, "contact.html")