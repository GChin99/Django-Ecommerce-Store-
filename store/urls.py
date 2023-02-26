from django.urls import path

from . import views #we need to connect the urls folder to the views folder.  The . is refering to the STORE folder since that is the folder the urls are in.

app_name = 'store' #app_name is matching the namespace path in the CORE urls folder

urlpatterns = [
    path('', views.product_all, name='product_all'),  #need to connect this path to the view
    path('<slug:slug>', views.product_detail, name='product_detail'), #need to connect this path to the view
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
