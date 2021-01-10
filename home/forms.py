from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from home.models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'location', 'password1', 'password2', )
