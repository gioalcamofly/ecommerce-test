from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class ReportsTestCase(TestCase):
    
    BASE_URL: str = 'api/v1'
    
    def setUp(self):
        pass
    
    def test_order_prices(self):
        
        client = APIClient()
        
        response = client.post(
            f'{self.BASE_URL}/reports/order-prices',
            None,
            format='json'
        )
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_product_customers(self):
            
        client = APIClient()
        
        response = client.post(
            f'{self.BASE_URL}/reports/product-customers',
            None,
            format='json'
        )
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_customer_ranking(self):
            
        client = APIClient()
        
        response = client.post(
            f'{self.BASE_URL}/reports/customer_ranking',
            None,
            format='json'
        )
                
        self.assertEqual(response.status_code, status.HTTP_200_OK)