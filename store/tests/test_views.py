from unittest import skip #this allows us to skip a test if we want

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.urls import reverse
from django.test import Client, RequestFactory, TestCase #this allows us to pretend we are a user testing our website

from store.models import Category, Product
from store.views import product_all

# an example of a test skip
# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        # Since we are not connected to the database we need some information to run the test 
        User.objects.create(username='admin')
        Category.objects.create(name='djang', slug='django') #we need the category to create a product
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')

# We are testing the homepage
    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200) #does the status_code = 200 which is ok.  404 would be page failed

# We are testing return reverse from the store_models.py file
# Since we are not connected to the database we need some information to run the test.  We put the information in the class setUp 
    def test_product_detail_url(self):
        """
        Test product response status
        """
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)


    def test_homepage_html(self):
        request = HttpRequest() #we can send a HttpRequest directly to one of our views
        response = product_all(request)
        html = response.content.decode('utf8') #the default code should be utf8
        print(html)
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

# testing using RequestFactory instead of Client. Request Factory tests it as a function instead of as a web browser the way Client does
    def test_view_function(self):
        request = self.factory.get('/django-beginners')
        response = product_all(request)
        html = response.content.decode('utf8') #the default code should be utf8
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)