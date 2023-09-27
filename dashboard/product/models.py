from django.db import models
from django.contrib.auth.models import PermissionsMixin
from core.abstract.models import AbstractModel, AbstractManager
from dashboard.shop.models import Shop

def img_directory_path(instance, filename):
	filename = instance.name
	return 'upload/product/images/{0}'.format(filename)

class ProductManager(AbstractManager):
	pass


class Product(AbstractModel):
	shop = models.ForeignKey(to="dashboard_shop.Shop", on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	product_type = models.CharField(max_length=100)
	description = models.CharField(max_length=400)
	price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
	is_available = models.BooleanField(default=True)
	stock = models.PositiveIntegerField(default=0)
	img = models.ImageField(upload_to=img_directory_path)
	img1 = models.ImageField(upload_to=img_directory_path)
	img2 = models.ImageField(upload_to=img_directory_path)

	objects = ProductManager()

	def __str__(self):
		return f"{self.name}"

	class Meta:
		db_table = "'dashboard.product'"

class CartManager(AbstractManager):
	pass

class Cart(AbstractModel):
	product = models.ManyToManyField(Product, blank=True)
	total= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

	objects = CartManager()

	def __str__(self):
		return f"{self.name}"

	class Meta:
		db_table = "'dashboard.cart'"

class CartItemManager(AbstractManager):
	pass

class CartItem(AbstractModel):
	cart=models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True,blank=True)
	product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
	quantity=models.IntegerField(default=1)

	objects = CartItemManager()

	def __str__(self):
		return f"{self.name}"

	class Meta:
		db_table = "'dashboard.cartitem'"

