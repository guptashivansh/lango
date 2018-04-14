from django.db import models


# Create your models here.
class TranslatorProfile(models.Model):
	full_name 		= models.CharField(max_length=50)
	occupation 		= models.CharField(max_length=50)
	cost_per_hour 	= models.IntegerField()
	country 		= models.CharField(max_length=50)
	#Languages_Known = models.MultipleChoiceField()
	bio 			= models.TextField(max_length=500, blank=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	activated		= models.BooleanField(default=False)


	def __str__(self):
		return self.user.username

	# def create_slug(instance, new_slug=None):
	# slug = slugify(instance.full_name)
	# if new_slug is not None:
	# 	slug = new_slug
	# qs = TranslatorProfile.objects.filter(slug=slug).order_by("-timestamp")
	# exists = qs.exists()
	# if exists:
	# 	new_slug = "%s-%s" %(slug, qs.first().timestamp)
	# 	return create_slug(instance, new_slug = new_slug)
	# return slug



# full name, 
# occupation, language fluency (multiple additions are possible), 
# estimated cost per hour, years of experience, country of residence, brief bio.




