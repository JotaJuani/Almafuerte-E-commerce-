from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este correo ya está registrado.')
        return email
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingresa nombre de usuario...'})
        self.fields['email'].label = 'Correo electrónico'
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingresa tu correo...'})
        self.fields['password1'].label = 'Contraseña'
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Ingresa tu contraseña...'})
        self.fields['password2'].label = 'Repetir contraseña'
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeti tu contraseña...'})
