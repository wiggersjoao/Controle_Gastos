
from users import views
from django.views.generic import TemplateView
from django.urls import path, include, re_path

urlpatterns = [
  re_path("login/", views.loginPage, name="login"),
  re_path("sign-up/", views.signUpPage, name="signUp"),
]