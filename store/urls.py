from django.urls import path

from . import views #we need to connect the urls folder to the views folder.  The . is refering to the STORE folder since that is the folder the urls are in.

app_name = 'store' #app_name is matching the namespace path in the CORE urls folder

urlpatterns = [
    path('', views.all_products, name='all_products'),  #need to connect this path to the view
    path('item/<slug:slug>/', views.product_detail, name='product_detail'), #need to connect this path to the view
]
