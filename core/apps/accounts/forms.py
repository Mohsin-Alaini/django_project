from typing import Any
from django import forms
from apps.models import Account, Currency,AccountType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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
        self.fields['code'].initial = 'oop'
        self.fields['code'].disabled = True 
    class Meta:
        model = Currency
        fields ="__all__"

class AccountTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'account_type'
        self.helper.form_id = 'form-id'
        self.helper.add_input(Submit(name='submit',value='submit',css_class='btn btn-info'))
        
        
    def clean_name(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data['name']  # if we want to get value from the dectionary
        name = cleaned_data.get('name')
        # self.add_error('name','hbvdchj')
        return name
    class Meta:
        model = AccountType
        fields ="__all__"
        
class AccountForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = '__all__'