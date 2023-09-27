from rest_framework.permissions import IsAuthenticated, AllowAny
from core.abstract.viewsets import AbstractViewSet
from dashboard.shop.serializers import ShopSerializer
from dashboard.shop.models import Shop
from dashboard.product.serializers import ProductSerializer
from dashboard.product.models import Product
from rest_framework import status, generics
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response

class ProductViewSet(AbstractViewSet):
	http_method_names = ('post', 'get', 'put', 'delete')
	permission_classes = (IsAuthenticated,)
	serializer_class = ProductSerializer

	def get_queryset(self):
		user = self.request.user
		if user.role == 'CUSTOMER':
			return Product.objects.all()
		sh_name = self.request.query_params.get('shop_name')
		sh = Shop.objects.get_object_by_public_id(sh_name)	
		obj = Product.objects.filter(shop=sh.id)
		return obj

	def get_object(self):
		obj = Product.objects.get_object_by_public_id(self.kwargs['pk'])
		self.check_object_permissions(self.request, obj)
		return obj

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductView(generics.ListCreateAPIView):
	serializer_class = ProductSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Product.objects.all()

	def perform_create(self, serializer):
		serializer.save()
