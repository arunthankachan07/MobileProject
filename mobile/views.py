from django.db.models import Sum
from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product,Order,Carts
from .forms import UserRegistrationForm,LoginForm,OrderForm,CartForm,ChangePasswordForm
from django.contrib.auth import authenticate,login,logout
from .decorators import login_required,user_admin
from .authentication import EmailAuthenticationBackend
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# Create your views here.
@login_required
def index(request):
    return render(request,"mobile/index.html")

@login_required
def listmobile(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)

@login_required
@user_admin
def add_product(request):
    form=ProductForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")

    return render(request,"mobile/createmobile.html",context)


def get_mobile_object(id):
    return Product.objects.get(id=id)

@login_required
def mobile_detail(request,id):
    mobile=get_mobile_object(id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobiledetail.html",context)


@login_required
@user_admin
def mobile_delete(request,id):
    mobile=get_mobile_object(id)
    mobile.delete()
    return redirect("list")

@login_required
@user_admin
def update_mobile(request,id):
    mobile=get_mobile_object(id)

    form=ProductForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method == "POST":
        form = ProductForm(request.POST,instance=mobile,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")

    return render(request,"mobile/edit_mobile.html",context)


def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            form=UserRegistrationForm(request.POST)
            context["form"]=form
    return render(request,"mobile/registration.html",context)

def login_user(request):
    context={}
    form=LoginForm()
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            obj=EmailAuthenticationBackend()

            user=obj.authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"mobile/index.html")

    return render(request,"mobile/login.html",context)

def signout(request):
    logout(request)
    return redirect("userlogin")

@login_required
def item_order(request,id):
    product=get_mobile_object(id)
    form=OrderForm(initial={'user':request.user,'product':product})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            context["form"]=form
            return render(request, "mobile/ordereditem.html", context)
    return render(request,"mobile/ordereditem.html",context)

@login_required
def view_my_orders(request):
    orders=Order.objects.filter(user=request.user)
    context={}
    context["orders"]=orders
    return render(request,"mobile/vieworders.html",context)


@login_required
def order_cancel(request,id):
    order=Order.objects.get(id=id)
    order.status='cancelled'
    order.save()
    return redirect("vieworder")

@login_required
def add_to_cart(request,id):
    product = get_mobile_object(id)
    form = CartForm(initial={'user': request.user, 'product': product})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            context["form"] = form
            return render(request, "mobile/mobiledetail.html", context)
    return render(request, "mobile/cartitem.html", context)

@login_required
def view_cart(request):
    cart_items=Carts.objects.filter(user=request.user)
    context={}
    context["cart_items"]=cart_items


    return render(request,"mobile/viewcart.html",context)

@login_required
def remove_cart_item(request,id):
    item = Carts.objects.get(id=id)
    if item.qty > 1:
        item.qty -= 1
        item.save()
        return redirect("viewcart")
    else:
        item.delete()
        return redirect("viewcart")

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #prevents from logging out after changing password
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changepassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'mobile/changepassword.html', {
        'form': form
    })