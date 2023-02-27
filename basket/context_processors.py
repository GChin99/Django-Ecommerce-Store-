from .basket import Basket #import the class Basket from the basket.basket.py file

def basket(request):
    return {'basket': Basket(request)}