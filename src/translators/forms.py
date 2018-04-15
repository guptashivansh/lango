from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model,login,logout

User = get_user_model()


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")

			if not user.is_active:
				raise forms.ValidationError("User no longer active")
		return super(UserLoginForm, self).clean(*args, **kwargs)


LANGUAGE_CHOICES = (
	('english','English'),
	('hindi','Hindi'),
	('french', 'French'),
	('spanish', 'Spanish'),
)
# class UserRegisterForm(forms.Form):
# 	username = forms.CharField()
# 	password   	= forms.CharField(widget = forms.PasswordInput)
# 	password2  	= forms.CharField(widget = forms.PasswordInput, label="Confirm password")
# 	full_name  	= forms.CharField(label="Full Name")
# 	occupation 	= forms.CharField()
# 	# language_fluency = forms.CharField()
# 	cost_per_hour = forms.IntegerField()
# 	country 	= forms.CharField(label='Country Of Residence')

# 	bio = forms.CharField(label='Bio', widget=forms.Textarea, required=False)

# 	Languages_Known = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.SelectMultiple,
#         choices=LANGUAGE_CHOICES,
#     )
# 	class Meta:
# 		model = User
# 		fields=[
# 			'username',
# 			'password',
# 			'password2',
# 			'full_name',
# 			'occupation',
# 			'Languages_Known',
# 			]
# 	def clean_password(self):
# 		password=self.cleaned_data.get("password")
# 		password2=self.cleaned_data.get("password2")
# 		# print(password2)
# 		if password == password2:
# 			print(password)
# 			print(password2)
# 			raise forms.ValidationError("Passwords must match")

# 		return password

class SignUpForm(UserCreationForm):

	# password   	= forms.CharField(widget = forms.PasswordInput)
	password2  	= forms.CharField(widget = forms.PasswordInput, label="Confirm password")


	full_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter a valid first name.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	occupation 	= forms.CharField()
	# language_fluency = forms.CharField()
	cost_per_hour = forms.IntegerField()
	country 	= forms.CharField(label='Country Of Residence')
	bio = forms.CharField(label='Bio', widget=forms.Textarea, required=False)
	Languages_Known = forms.MultipleChoiceField(
		required=False,
		widget=forms.SelectMultiple,
		choices=LANGUAGE_CHOICES,
	)
	class Meta:
		model = User
		fields = ('username', 'full_name',  'email', 'password1', 'password2',
			'occupation','cost_per_hour','country','Languages_Known','bio',
		 )
