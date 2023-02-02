from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model






class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'



class RegisterUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]







class Communiquons_projetForm(ModelForm):
    class Meta:
        model = Communiquons_projet
        fields = '__all__'





class Soumission_clienForm(ModelForm):
    class Meta:
        model = Soumission_client
        fields = '__all__'



class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'



