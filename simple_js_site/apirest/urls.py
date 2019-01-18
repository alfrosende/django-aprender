from django.urls import path
from apirest import views

urlpatterns = [
    path('apirest/', views.home, name='home'),
    path('apirest/login', views.loginopus, name='login'),
]