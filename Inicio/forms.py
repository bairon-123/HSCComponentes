from django import forms

from Inicio.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombreproducto': forms.TextInput(attrs={'class': 'form-control'}),
            'precioproducto': forms.NumberInput(attrs={'class': 'form-control'}),
            'especificacionprod': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'stockprod': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagenprod': forms.FileInput(attrs={'class': 'form-control'}),
            'tipoprod': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.Select(attrs={'class': 'form-select'}),
        }

        