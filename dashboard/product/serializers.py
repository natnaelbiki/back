from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer
from .models import Product
from dashboard.shop.models import Shop
from core.user.models import User
from dashboard.shop.serializers import  ShopSerializer


class ProductSerializer(AbstractSerializer):
	shop = serializers.SlugRelatedField(queryset=Shop.objects.all(), slug_field='name')

	class Meta:
		model = Product
		fields = ['id', 'name', 'product_type', 'description', 'shop', 'price', 'img', 'img1', 'img2']