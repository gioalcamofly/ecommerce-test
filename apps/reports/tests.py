from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class ReportsTestCase(APITestCase):
        
    def test_upload_data(self):
        
        url = reverse('upload-reports')
        response = self.client.post(url, {'test': 'test'}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_order_prices(self):
        
        url = reverse('order-prices')
        response = self.client.get(url)
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRegex(response.headers['Content-Type'], 'text/csv')
        
    def test_product_customers(self):
        
        url = reverse('product-customers')
        response = self.client.get(url)
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRegex(response.headers['Content-Type'], 'text/csv')
        
    def test_customer_ranking(self):
        
        url = reverse('customer-ranking')
        response = self.client.get(url)
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRegex(response.headers['Content-Type'], 'text/csv')