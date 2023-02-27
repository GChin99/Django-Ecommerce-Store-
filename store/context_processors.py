from .models import Category #import class Category from store.models.py folder 

def categories(request):
    return {
        'categories': Category.objects.all()
    }
    # We want to make this available on all pages.  We need to add the views to the context_processeors in the CORE setting.py file
