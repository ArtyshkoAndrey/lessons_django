from django import forms
from .models import Brand


class BrandValidate(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description']
