from django.urls import path
from . import views
from .views import RegistroView, loginView

urlpatterns = [
    path('', RegistroView.as_view(), name="registro"),
    path('login/', views.loginView, name="login"),
]