from django import forms
from .models import Vegetables


class VegetableCreateForm(forms.ModelForm):
    class Meta:
        model = Vegetables
        exclude = ["category"]
