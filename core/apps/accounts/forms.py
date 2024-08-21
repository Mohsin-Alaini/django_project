from typing import Any
from django import forms

class InfonForm(forms.Form):
    name = forms.CharField(label="name",max_length=50)
    number = forms.IntegerField(label='number',max_value=100,min_value=1)
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data