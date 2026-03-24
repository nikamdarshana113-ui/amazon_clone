from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query) if query else Product.objects.all()
    return render(request, 'home.html', {'products': products})

@login_required
def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity += 1
    item.save()
    return redirect('/')

@login_required
def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'items': items})

@login_required
def place_order(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    order = Order.objects.create(user=request.user)

    for item in items:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

    items.delete()
    return redirect('/orders/')

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})

def dashboard(request):
    return render(request, 'dashboard.html')

def checkout(request):
    return render(request, 'checkout.html')