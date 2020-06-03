from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=30)
	image = models.ImageField(upload_to='Pictures',null=True)

	def __str__(self):
		return self.user.username