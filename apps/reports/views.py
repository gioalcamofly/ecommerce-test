from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import status
import csv

from rest_framework_csv import renderers as r

from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer, UploadReportSerializer
from .services import reports_service


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'
    
class UploadDataView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UploadReportSerializer(data=request.data)
        if serializer.is_valid():
            reports_service.upload_data(request.data)
            return Response('', status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderPricesView(APIView):
        
    def get(self, request: Request) -> HttpResponse:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="order_prices.csv"'
        writer = csv.writer(response)
        writer.writerow(['Order ID', 'Order Price'])
        writer.writerows([
            [order_price['order_id'], order_price['total_price']] for order_price in reports_service.order_prices()
        ])
        
        return response
    
class ProductCustomersView(APIView):
    
    def get(self, request: Request) -> HttpResponse:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="product_customers.csv"'
        writer = csv.writer(response)
        writer.writerow(['Product ID', 'Customer IDs'])
        writer.writerows([
            [product_customer['product_id'], product_customer['customer_ids']] for product_customer in reports_service.product_customers()
        ])
        
        return response
    
class CustomerRankingView(APIView):
    
    def get(self, request: Request) -> HttpResponse:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="customer_ranking.csv"'
        writer = csv.writer(response)
        writer.writerow(['Customer ID', 'Customer Name', 'Customer Lastname', 'Total'])
        writer.writerows([
            [
                customer['customer_id'], customer['customer_name'], 
                customer['customer_lastname'], customer['total_price']
            ] for customer in reports_service.customer_ranking()
        ])
        
        return response