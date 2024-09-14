from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, label="Nombre")
    email = forms.EmailField(label="Mail")
    content = forms.CharField(widget=forms.Textarea, label="Mensaje")


class PlantillasForm(forms.Form):
    email = forms.EmailField()
