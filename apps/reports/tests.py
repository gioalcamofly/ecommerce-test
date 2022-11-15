from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework import status

from .utils.custom_assertions import CsvAssertionMixin

import csv
import io

# Create your tests here.
class ReportsTestCase(APITestCase, CsvAssertionMixin):
        
    def test_upload_data(self):
        
        url = reverse('upload-reports')
        customers = SimpleUploadedFile('customers.csv', b"test", content_type='text/csv')
        products = SimpleUploadedFile('products.csv', b"test", content_type='text/csv')
        orders = SimpleUploadedFile('orders.csv', b"test", content_type='text/csv')
        
        data = {
            'customers': customers,
            'products': products,
            'orders': orders
        }
        
        response = self.client.post(url, data, format='multipart')
                
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_order_prices(self):
        
        url = reverse('order-prices')
        response = self.client.get(url)
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRegex(response.headers['Content-Type'], 'text/csv')

        content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(content))
        self.assertHeadersExist(csv_reader, 'Order ID', 'Order Price')
        
        
        
    def test_product_customers(self):
        
        url = reverse('product-customers')
        response = self.client.get(url)
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRegex(response.headers['Content-Type'], 'text/csv')
        
        content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(content))
        self.assertHeadersExist(csv_reader, 'Product ID', 'Customer IDs')
        
    def test_customer_ranking(self):
        
        url = reverse('customer-ranking')
        response = self.client.get(url)
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRegex(response.headers['Content-Type'], 'text/csv')
        
        content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(content))
        self.assertHeadersExist(csv_reader, 'Customer ID', 'Customer Name', 'Customer Lastname', 'Total')