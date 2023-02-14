from django.shortcuts import render

from .models import Category, Product

# Create your views here.
def all_products(request): #request is the request the user is making on the web broswer
    products = Product.objects.all() #this is a query for the database.  Its the same as the SQL query select all 
    return render(request, 'store/home.html', {'products': products}) #this is the template we want to display (store/home.html) and what data we want to display on the template (products)