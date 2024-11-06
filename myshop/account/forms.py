from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingresa nombre de usuario...'})
        self.fields['password1'].label = 'Contraseña'
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingresa tu contraseña...'})
        self.fields['password2'].label = 'Repetir contraseña'
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeti tu contraseña...'})
