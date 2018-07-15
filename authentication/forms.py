from django import forms

class newUserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField()
    username = forms.CharField(label = "User Name", max_length = 100)
    password = forms.CharField(label = "Password", max_length = 100)


class loginForm(forms.Form):
    username = forms.CharField(label = "User Name", max_length = 100)
    password = forms.CharField(label = "Password", max_length = 100)
