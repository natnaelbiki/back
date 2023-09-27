from rest_framework_nested import routers

from dashboard.shop.viewsets import ShopViewSet
from dashboard.product.viewsets import ProductViewSet

router = routers.SimpleRouter()

router.register(r'shop', ShopViewSet, basename='shop')
router.register(r'product', ProductViewSet, basename='product')



urlpatterns = [
	*router.urls,
]