from django.urls import path, include

from . import views

urlpatterns = [
    path('join', views.register.as_view()),
    path('login', views.loginUser.as_view()),

]
