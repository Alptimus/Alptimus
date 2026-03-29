
# User registration

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Profile

# User login

from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput

from django import forms


# User registration
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = {'username', 'email', 'password1', 'password2'}


# Login users
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Profile management - Update 
class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:

        model = User

        fields = ['username', 'email']
        exclude = ['password1', 'password2']



# Updating our profile picture

class UpdateProfileForm(forms.ModelForm):

    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:

        model = Profile
        fields = ['profile_pic']

