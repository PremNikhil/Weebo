
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Art, Clothing, Laptop_Cover, Mobile_Cover


def home(request):
    return render(request, 'ecommerce/home.html')


def about(request):
    return render(request, 'ecommerce/about.html')


@login_required
def cart(request):
    return render(request, 'ecommerce/cart.html')



@login_required
def ordered(request):
    return render(request, 'ecommerce/order_succesfull.html')

@login_required
def myorders(request):
    return render(request, 'ecommerce/orders.html')

def mobile_cover(request):
    context={
        'mobile_covers': Mobile_Cover.objects.all()
    }
    return render(request, 'ecommerce/mobile_covers.html', context)


def laptop_cover(request):
    context={
        'laptop_covers': Laptop_Cover.objects.all()
    }
    return render(request, 'ecommerce/laptop_covers.html', context)


def art(request):
    context={
        'arts': Art.objects.all()
    }
    return render(request, 'ecommerce/art.html', context)




def clothing(request):
    context={
        'clothings': Clothing.objects.all()
    }
    return render(request, 'ecommerce/clothes.html', context)








