from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save

User= settings.AUTH_USER_MODEL


# Create your models here.
class TranslatorProfile(models.Model):
	name 			= models.OneToOneField(User, on_delete=models.CASCADE)
	occupation 		= models.CharField(max_length=50,null=True,blank=True)
	country 		= models.CharField(max_length=50,null=True,blank=True)
	cost_per_hour 	= models.IntegerField(default=0)
	Languages_Known = models.CharField(max_length=50,null=True,blank=True)
	bio 			= models.TextField(max_length=500, blank=True)
	
	# def __str__(self):
	#  	return self.name

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

# def pre_save_receiver(sender, instance, *args, **kwargs):
# 	print("Saving..")
# 	print(instance.country)
# 	instance.save()

# pre_save.connect(pre_save_receiver, sender=TranslatorProfile)
