from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)
    class Meta:
        model = User
        fields = ('username','email','role')
