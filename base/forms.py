from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class RegisterForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    twitter_username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # mob = forms.CharField(max_length=13)
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM--DD')
    # gender = forms.CharField(max_length=17)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'twitter_username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'username', 'email', 'twitter_username' ,'bio']
        