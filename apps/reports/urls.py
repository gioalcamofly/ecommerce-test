from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CustomerViewSet, ProductViewSet, OrderViewSet, \
                   OrderPricesView, ProductCustomersView, CustomerRankingView, \
                   UploadDataView

router = DefaultRouter()

router.register('customers', CustomerViewSet, basename='customers')
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('reports', UploadDataView.as_view(), name='upload-reports'),
    path('reports/order-prices', OrderPricesView.as_view(), name='order-prices'),
    path('reports/product-customers', ProductCustomersView.as_view(), name='product-customers'),
    path('reports/customer-ranking', CustomerRankingView.as_view(), name='customer-ranking')
]

urlpatterns += router.urls