import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm        

from django.http import JsonResponse
from django.db.models import Q
# registeration form
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'account successfully created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'authentication/user_register.html', context)
# login form 
def user_login(request):
    if request.method== 'POST':
        forms = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            customer = Customer(user=user)
            customer.save()        
        except:
            messages.info(request, 'username does not exits')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Invalid username or password')
        else:
            login(request, user)
            return redirect('store')
    else:
        forms = AuthenticationForm()
    context = {'forms':forms}
        
    return render(request, 'authentication/user_login.html', context)
# logout view
def user_logout(request):
    logout(request)
    return redirect('login')

def checkout(request):
    cartItems = None
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'live/checkout.html', context)

def cart(request):
    cartItems = None
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items  
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'live/cart.html', context)

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'live/store.html', context)

def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('item was added', safe=False)

def MakeOrder(request):
    print('Data', request.body)
    return JsonResponse('Payment complete', safe=False)

def search(request):
    
    q = request.GET.get('q', '')
    items = Product.objects.filter(Q(name__icontains = q)|Q(description__icontains = q))
    context = {'q':q , 'items':items}
    return render(request, 'live/search.html', context)
























# @receiver(user_logged_in)            
# def user_is_logged_in(sender, request, **kwargs):
#     messages.add_message(request, messages.INFO, 'Hi @' + request.user.username + 'welcome')
#     return render(request, 'live/user_is_logged_in')
