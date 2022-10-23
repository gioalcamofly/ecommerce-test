from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, ProductViewSet, OrderViewSet

router = DefaultRouter()

router.register('customers', CustomerViewSet, basename='customers')
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = router.urls