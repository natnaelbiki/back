from django.db import models
from django.contrib.auth.models import PermissionsMixin
from core.abstract.models import AbstractModel, AbstractManager

# Create your models here.

class ShopManager(AbstractManager):
	pass

class Shop(AbstractModel):
	owner = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	location = models.CharField(max_length=255)
	shop_type = models.CharField(max_length=100)
	description = models.CharField(max_length=400)

	objects = ShopManager()

	def __str__(self):
		return f"{self.name}"

	class Meta:
		db_table = "'dashboard.shop'"