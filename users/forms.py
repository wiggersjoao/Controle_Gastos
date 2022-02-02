from django.contrib.auth import forms

from .models import User 

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm):
        model = User
        forms = '__all__'
        exclude = '',

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm):
        model = User
        forms = '__all__'
        exclude = '',