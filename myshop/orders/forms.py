from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name',
                  'last_name',
                  'email',
                  'address',
                  'postal_code',
                  'city',]
        
        labels = {'first_name': 'Nombre',
                  'last_name': 'Apellido',
                  'email': 'mail',
                  'address': 'Dirección',
                  'postal_code': 'Código postal',
                  'city': 'Ciudad',
                  }
