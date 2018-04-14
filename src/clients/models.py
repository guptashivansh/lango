from django.db import models

# Create your models here.

class ClientProfile(models.Model):
	first_name = models.CharField(max_length=50)
	last_name  = models.CharField(max_length=50, null=True)


	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	activated		= models.BooleanField(default=False)

	def __str__(self):
		return self.user.username



