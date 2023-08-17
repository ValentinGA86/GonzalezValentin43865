from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuariosForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)
    empresa = forms.CharField(label="Empresa u organización", max_length=50, required=False)
    website = forms.URLField(label="Website", max_length=50, required=False)
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    imagen = forms.ImageField(required=False)  

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'empresa', 'website']
        help_texts = {k:"" for k in fields}    


class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)
    empresa = forms.CharField(label="Empresa u organización", max_length=50, required=False)
    website = forms.URLField(label="Website", max_length=50, required=False)
    email = forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
       model = User
       fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'empresa', 'website']
       help_texts = {k:"" for k in fields}    
       
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)  