from django.db import models


# Create your models here.
class TranslatorProfile(models.Model):
	first_name 		= models.CharField(max_length=50)
	last_name  		= models.CharField(max_length=50, null=True)

	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	activated		= models.BooleanField(default=False)
	bio 			= models.TextField(max_length=500, blank=True)

	def __str__(self):
		return self.user.username



# full name, 
# occupation, language fluency (multiple additions are possible), 
# estimated cost per hour, years of experience, country of residence, brief bio.




