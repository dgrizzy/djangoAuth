from django.http import HttpResponse
from django.shortcuts import render

# Imoprt the View Class for our CBV
from django.views import View

# Import Assets
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class register(View):
        def get(self, request):

            newUserForm = forms.newUserForm()

            return render(request, "signUp.html", context = {"newUserForm" : newUserForm})

        def post(self, request):

            formData = forms.newUserForm(request.POST)

            if formData.is_valid():

                newUser = User.objects.create_user(formData.cleaned_data["username"],
                                                   email = formData.cleaned_data["email"],
                                                   password = formData.cleaned_data["password"])

                newUser.last_name = formData.cleaned_data["last_name"]
                newUser.first_name = formData.cleaned_data["first_name"]

                newUser.save()

                return HttpResponse("Thanks!")
            else:
                return HttpResponse("Try again!")


class loginUser(View):
    def get(self, request):

        loginForm = forms.loginForm()

        return render(request, "signIn.html", context = {'loginForm' : loginForm})

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return HttpResponse("Success")
        else:
            return HttpResponse("Authentication Failed")
