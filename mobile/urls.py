"""mobileProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import index,listmobile,add_product,mobile_detail,update_mobile,registration,login_user,\
    signout,mobile_delete,item_order,view_my_orders,order_cancel,view_cart,add_to_cart,\
    remove_cart_item,change_password



urlpatterns = [

path("listmobile",listmobile,name="list"),
path("addproduct",add_product,name="addproduct"),
path("mobiles/<int:id>",mobile_detail,name="detail"),
path("update/<int:id>",update_mobile,name="edit"),
path("registration",registration,name="register"),
path("login",login_user,name="userlogin"),
path("userhome",index,name="userhome"),
path("logout",signout,name="signout"),
path("delete/<int:id>",mobile_delete,name="delete"),
path("itemorderd/<int:id>",item_order,name="order"),
path("vieworder",view_my_orders,name="vieworder"),
path("cancelorder/<int:id>",order_cancel,name="cancel_order"),
path("addtocart/<int:id>",add_to_cart,name="addtocart"),
path("viewcart",view_cart,name="viewcart"),
path("removeitem/<int:id>",remove_cart_item,name="removeitem"),
path("changepassword",change_password,name="changepassword"),

]
