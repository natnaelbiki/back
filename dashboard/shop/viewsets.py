from rest_framework.permissions import IsAuthenticated, AllowAny
from core.abstract.viewsets import AbstractViewSet
from dashboard.shop.serializers import ShopSerializer
from dashboard.shop.models import Shop
from rest_framework import status
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response

class ShopViewSet(AbstractViewSet):
	http_method_names = ('post', 'get', 'put', 'delete')
	permission_classes = (IsAuthenticated,)
	serializer_class = ShopSerializer

	def get_queryset(self):
		user = self.request.user
		if user.is_superuser:
			return Shop.objects.all().order_by('name')
		return Shop.objects.filter(owner=user)

	def get_object(self):
		obj = Shop.objects.get_object_by_public_id(self.kwargs['pk'])
		self.check_object_permissions(self.request, obj)
		return obj

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)