from django.db import models
import uuid
from core.abstract.models import AbstractModel, AbstractManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

ROLE = (
	('ADMIN', 'Admin'),
	('SUPPLIER', 'Supplier'),
	('CUSTOMER', 'Customer'),
	('DELIVERY', 'Delivery'),
	)
class UserManager(BaseUserManager, AbstractManager):
	def get_object_by_public_id(self, public_id):
		try:
			instance = self.get(public_id=public_id)
			return instance
		except (ObjectDoesNotExist, ValueError, TypeError):
			return Http404

	def create_user(self, username, email, password=None, **kwargs):
		if username is None:
			raise TypeError('User must have a username.')
		if email is None:
			raise TypeError('User must have an email.')
		if password is None:
			raise TypeError('User must have an password')

		user = self.model(username=username,
			email=self.normalize_email(email), **kwargs)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, username, email, password, **kwargs):
		if password is None:
			raise TypeError('Superusers must have a password.')

		if email is None:
			raise TypeError('Superusers must have an email')

		if username is None:
			raise TypeError('Superusers must have an username')

		user = self.create_user(username, email, password,
			**kwargs)
		user.is_superuser = True
		user.is_staff = True
		user.role = 'Admin'
		user.save(using=self._db)

		return user

# User Model
class User(AbstractModel ,AbstractBaseUser, PermissionsMixin):
	username = models.CharField(db_index=True,
		max_length=255, unique=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(db_index=True, unique=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=True)
	role = models.CharField(choices=ROLE, max_length=10, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = ['username']

	objects = UserManager()

	def __str__(self):
		return f"{self.email}"

	@property
	def name(self):
		return f"{self.first_name} {self.last_name}"

