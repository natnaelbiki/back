from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.abstract.serializers import AbstractSerializer

from dashboard.shop.models import Shop
from core.user.models import User
from core.user.serializers import  UserSerializer


class ShopSerializer(AbstractSerializer):
	owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')

	def validate_owner(self, value):
		if self.context["request"].user != value:
			raise ValidationError("You can't create a Shop for another person")
		return value

	def to_representation(self, instance):
		rep = super().to_representation(instance)
		owner = User.objects.get_object_by_public_id(rep['owner'])
		rep['owner'] =  UserSerializer(owner).data

		return rep
	def update(self, instance, validated_data):
		instance = super().update(instance, validated_data)
		return instance

	class Meta:
		model = Shop
		fields = ['id', 'name', 'location', 'shop_type', 'description', 'owner']