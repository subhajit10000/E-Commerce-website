import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import CustomUser, Product, CartItem, Category, Order
from . forms import MyRegFrm, MyLogFrm
# Create your views here.

def home(request):
    products=Product.objects.all()
    return render(request, 'myapp/home.html', {'products':products})


def userlog(request):
    return render(request, 'myapp/log.html')

def product(request):
    allcat=Category.objects.all()
    return render(request, 'myapp/product.html', {'allcat':allcat})

def cat_product(request,cat_id):
     cat_product = cat_product.objects.get(name=cat_id)
     allprod=Product.objects.filter(id=cat_id).values()
     return render (request, 'myapp/cat_product.html', {'allprod':allprod, 'cat_product':cat_product})




def contact(request):
    return render(request, 'myapp/contact.html')


def userReg(request):
    if request.POST:
        form=MyRegFrm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registration is successfull')
            except Exception :
                messages.error(request, 'Registration is unsuccessfull')
    else:
        form=MyRegFrm()
    return render(request, 'myapp/reg.html',{'form':form})


def userLog(request):
    if request.POST:
        form=MyLogFrm(request=request, data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/')
        
    else:
        form=MyLogFrm()
    return render(request, 'myapp/log.html', {'form':form})

def userLogout(request):
    logout(request)
    return redirect('/login/')

def add_to_cart(request, product_id):
	if request.user.is_authenticated:
		product = Product.objects.get(id=product_id)
		cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                        user=request.user)
		cart_item.quantity += 1
		cart_item.save()
		return redirect('/cart')
	else:
		return redirect('/login')

def view_cart(request):
	if request.user.is_authenticated:
		cart_items = CartItem.objects.filter(user=request.user)
		total_price = sum(item.product.price * item.quantity for item in cart_items)
		total_price=int(total_price)
		return render(request, 'myapp/cart.html', {'cart_items': cart_items, 'total_price': total_price})
	else:
		return redirect('/login')
     
def remove_cart(request,id):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(id=id, user=request.user)
        cart_item.delete()
        return redirect('/cart')
    else:
        return redirect('/login')
    




    
    
def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST["amount"]) * 100  # Amount in paise
        address=request.POST['address']
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

        payment_data = {
            "amount": amount,
            "currency": "INR",
            "receipt": "order_receipt",
            "notes": {
                "email": "user_email@example.com",
            },
        }

        order = client.order.create(data=payment_data)
        
        # Include key, name, description, and image in the JSON response
        response_data = {
            "id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "key": settings.RAZORPAY_API_KEY,
            "name": "My Project",
            "description": "Payment for Your Product",
            "image": "https://yourwebsite.com/logo.png",  # Replace with your logo URL
        }
        cart_items=CartItem.objects.filter(user=request.user)
        # payment_id=response_data.id
        for cart in cart_items:
            Order.objects.get_or_create(user=request.user, product= cart.product, quantity=cart.quantity, payment_status='success', address=address)
        
        CartItem.objects.filter(user=request.user).delete()

        return JsonResponse(response_data)
    return redirect('myapp:viewCart.html')

def payment_success(request):
    return render(request, "myapp/payment_success.html")

def payment_failed(request):
    return render(request, "myapp/payment_failed.html")


def myOrders(request):
    if request.user.is_authenticated:
        allord=Order.objects.filter(user=request.user)
        return render(request, 'myapp/viewOrders.html',{'orderItems':allord})
    else:
        return redirect('/login')




def smartphones(request):
    return render(request, 'myapp/smartphones.html')
def home_appliances(request):
    return render(request, 'myapp/home_appliances.html')
def camera(request):
    return render(request, 'myapp/camera.html')
def other_electronic_gadget(request):
    return render(request, 'myapp/other_electronic_gadget.html')
def iot_components(request):
    return render(request, 'myapp/iot_components.html')
def laps_tab(request):
    return render(request, 'myapp/laps_tab.html')
def watch(request):
    return render(request, 'myapp/watch.html')

