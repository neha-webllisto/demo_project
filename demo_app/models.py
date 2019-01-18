from django.db import models

# Create your models here.
class Register(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	subject = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	address = models.CharField(max_length=50)


class Login(models.Model):
	username = models.EmailField(max_length=20)
	password = models.CharField(max_length=20)
