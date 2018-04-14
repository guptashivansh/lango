from django import forms
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



class UserRegisterForm(forms.ModelForm):
	password   	= forms.CharField(widget = forms.PasswordInput)
	password2  	= forms.CharField(widget = forms.PasswordInput, label="Confirm password")
	full_name  	= forms.CharField(label="Full Name")
	occupation 	= forms.CharField()
	language_fluency = forms.CharField()
	# bio = forms.TextField(max_length=500, null=True)




	class Meta:
		model = User
		fields=[
			'username',
			'password',
			'password2'

			]
	def clean_password(self):
		password=self.cleaned_data.get("password")
		password2=self.cleaned_data.get("password2")
		# print(password2)
		if password == password2:
			print(password)
			print(password2)
			raise forms.ValidationError("Passwords must match")

		return password
