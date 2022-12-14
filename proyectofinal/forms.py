from django import forms
class Buscar(forms.Form):
    empresa = forms.CharField(max_length=100)