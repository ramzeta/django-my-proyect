from django.contrib.auth.forms import UserCreationForm
from .models import IrisData
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class IrisDataForm(forms.ModelForm):
    class Meta:
        model = IrisData
        fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']