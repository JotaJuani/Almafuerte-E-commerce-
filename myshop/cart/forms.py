from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 9)]
PRODUCT_SIZE_CHOICES = [(i, str(i)) for i in range(1, 7)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int,
                                      label=_('Cant'),
                                      widget=forms.Select(attrs={
                                          'class': 'cantidad-control',
                                          'style': 'width: 80px;',
                                      })
                                      )
    size = forms.TypedChoiceField(choices=PRODUCT_SIZE_CHOICES,
                                  required=False,
                                  coerce=int,
                                  label=_('Talle'),
                                  widget=forms.Select(attrs={
                                      'class': 'cantidad-control',
                                      'style': 'width: 80px;',
                                  }))
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
