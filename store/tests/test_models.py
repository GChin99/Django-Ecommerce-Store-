from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product
# Create your tests here.

class TestCategoriesModel(TestCase): 
# Creating the sample test data to use. Since this is testing the category model we only need two data entries 
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')
# Testing the category entry.  Does the name match the slug
    def test_category_model_entry(self):
        """
        Test category model data insertation/type/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
# Testing the return self.name statment from the class Category in the models file 
    def test_category_model_entry(self):
        """
        Test category model default name
        """
        data= self.data1
        self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):
#Creating the sample test data for the products.  Since this has more entries than the Category models we need more data entries
    def setUp(self):
        Category.objects.create(name='djang', slug='django') #we need the category to create a product
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')


    def test_products_model_entry(self):
        """
        Test category model data insertation/type/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners') #were testing the product.models return statement.  It should return the products title