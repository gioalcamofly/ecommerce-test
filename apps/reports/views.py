from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

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
    def post(self, request):
        serializer = UploadReportSerializer(data=request.data)
        if serializer.is_valid():
            reports_service.upload_data(request.data)
            return Response('', status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderPricesView(APIView):
    
    renderer_classes = (r.CSVRenderer,)
    
    def get(self, request):
        order_prices = reports_service.order_prices()
        return Response(order_prices, status=status.HTTP_200_OK)
    
class ProductCustomersView(APIView):
    
    renderer_classes = (r.CSVRenderer,)
    
    def get(self, request):
        product_customers = reports_service.product_customers()
        return Response('', status=status.HTTP_200_OK)
    
class CustomerRankingView(APIView):
    
    renderer_classes = (r.CSVRenderer,)
    
    def get(self, request):
        customer_ranking = reports_service.customer_ranking()
        return Response('', status=status.HTTP_200_OK)