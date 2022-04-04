from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from weather.models import City


class SignUpForm(UserCreationForm):
    country = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'country', 'password1', 'password2')


class CityForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"Placeholder": 'search ...'}))

    class Meta:
        model = City
        fields = ('name',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
