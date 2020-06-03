from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Lawyer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	buisness_address = models.CharField(max_length=100)
	about = models.CharField(max_length=300,null=True)
	contact = models.CharField(max_length=300,null=True)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=30)
	liscence_number = models.IntegerField()
	year_admitted = models.DateTimeField()
	hcr_number = models.IntegerField(unique=True)
	image = models.ImageField(upload_to='Pictures',null=True)

	# Type = models.CharField(max_length=30,default="lawyer",null=False)
	rate = models.IntegerField(
		default=5,
		validators=[MaxValueValidator(5), MinValueValidator(1)]
		)

	def __str__(self):
		return self.user.username + " " + str(self.rate)