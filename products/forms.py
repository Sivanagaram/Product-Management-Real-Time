from django import forms

from .models import products

class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields ='__all__'
        widgets = {
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            # 'is_published' : forms.BooleanField(attrs={'class': 'form-control'}),

        }


