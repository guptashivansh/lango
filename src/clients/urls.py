from django.urls import path
from django.contrib import admin

from .views import testview,login_view,register_view,logout_view

app_name="clients"

urlpatterns = [
    
    path('', testview),
    path('login/',login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
