from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EspecialidadesFormulario(forms.Form):
    
    especialidad = forms.CharField()
    adulto = forms.BooleanField()
    pediatrico = forms.BooleanField()

class StaffFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']
       help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}



