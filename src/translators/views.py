from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, get_user_model,login,logout
from django.shortcuts import render, redirect


from .forms import UserLoginForm,SignUpForm
from .models import TranslatorProfile
# Create your views here.


def testview(request):
	return HttpResponse("<h1> Done Deal</h1>")


def login_view(request):
	form = UserLoginForm(request.POST or None)
	title = "Login"
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		print(request.user.is_authenticated)
		return redirect("/")

	return render(request,"form_login.html",{'form':form,'title':title})

def register_view(request):
	title ="Register"
	form = SignUpForm(request.POST or None)
	if request.method == 'POST':
		# Get form data.
		
		if form.is_valid():
			user = form.save()
			user.save()
			#login the user
			password = form.cleaned_data.get("password")
			new_user = authenticate(username=user.username,password=password)
			login(request,new_user)
			return redirect("/")
	context = {"form":form, "title":title}
	return render(request,"form_register.html", context)

def logout_view(request):
	logout(request)
	return redirect("/")