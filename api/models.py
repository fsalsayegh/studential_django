from django.db import models
from django.contrib.auth.models import AbstractUser ,UserManager
# from django.contrib.auth.models import User



class Major(models.Model):
	name = models.CharField(max_length=120)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=120)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class User(AbstractUser):
	major = models.ForeignKey(Major, on_delete=models.PROTECT)
	course = models.ManyToManyField(Course)