from django.shortcuts import get_object_or_404, render 
# get_object_or_404 will either get the object requested and return it or if it can't, it will return 404

from .models import Category, Product

# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }
    # We want to make this available on all pages.  We need to add the views to the context_processeors in the CORE setting.py file

def all_products(request): #request is the request the user is making on the web broswer
    products = Product.objects.all() #this is a query for the database.  Its the same as the SQL query select all 
    return render(request, 'store/home.html', {'products': products}) #this is the template we want to display (store/home.html) and what data we want to display on the template (products)

# we are going to get an individual object from the data base
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True) #if the item is not in stock, it will not show the item
    return render(request, 'store/products/detail.html', {'product':product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category) #using a sql query to filter through all product's category that match the category_slug from the line above
    return render(request, 'store/products/category.html', {'category':category, 'products':products})