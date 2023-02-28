from django.contrib import admin
from .models import *


@admin.register(Maincategory)
class MainCategory(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Subcategory)
class SubCategory(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Brand)
class Brand(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("id", "name","maincategory","subcategory","brand","color","size","baseprice","discount","finalprice","stock","pic1","pic2","pic3","pic4")

@admin.register(Buyer)
class Buyer(admin.ModelAdmin):
    list_display = ("id","name","username","email","phone","addressline1","addressline2","addressline3","pin","city","state","pic")

@admin.register(CheckoutProducts)
class CheckoutProducts(admin.ModelAdmin):
    list_display = ("id","checkout","pid","name","color","size","price","qty","total","pic")

@admin.register(Checkout)
class Checkout(admin.ModelAdmin):
    list_display = ("id","user","orderStatus","paymentStatus","paymentMode","rppid","totalAmount","shippingAmount","finalAmount","time")

@admin.register(Wishlist)
class Wishlist(admin.ModelAdmin):
    list_display = ("id", "product","user")

@admin.register(ContactUs)
class ContactUs(admin.ModelAdmin):
    list_display = ("id", "name","email","phone","subject","message","status","time")

