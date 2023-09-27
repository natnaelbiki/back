from django.db import models
from django.contrib.auth.models import PermissionsMixin
from core.abstract.models import AbstractModel, AbstractManager
from core.user.models import User
from dashboard.product.models import Product

STATUS = (
	('ordered', 'Ordered'),
	('delivered', 'Delivered'),
	)
class OrderManager(AbstractManager):
	pass

class Order(AbstractModel):
	owner = models.ForeignKey(User, on_delete=models.PROTECT)
	product = models.ManyToManyField(Product, blank=False)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	is_active = models.BooleanField(default=True)

	objects = OrderManager()

	def __str__(self):
		return str(self.owner)