from typing import Any
from django import forms
from apps.models import Currency

class InfonForm(forms.Form): 
    name = forms.CharField(label="name",max_length=50)
    number = forms.IntegerField(label='number',max_value=100,min_value=1)
    
    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get('number')
        cleaned_data['number'] = 150
        print(cleaned_data,'cleaned_data')
        
        return cleaned_data
    
    def clean_number(self):
        cleaned_data = super().clean()
        if cleaned_data['number'] >=1 and cleaned_data['number'] <=20 :
            return cleaned_data['number']
        
        else :
            self.add_error('number','the number most be greater than 0 and smallest or equal than 20 . ')
            

CHOICES=[
    ('YER','YER'),
    ('SAR','SAR'),
]
class CurrencyForm(forms.ModelForm):
    # code = forms.CharField( label='code',widget=forms.Select(choices=CHOICES), required=True)
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].label = 'code'
    class Meta:
        model = Currency
        fields ="__all__"

