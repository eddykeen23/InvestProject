from django import forms

from .models import etf, account

class etf_form(forms.ModelForm):
    class Meta:
        model = etf
        fields = ['symbol', 'name']
        labels = {'symbol': 'Symbol:', 'name': 'Name:'}

class account_form(forms.ModelForm):
    class Meta:
        model = account
        fields = ['name', 'type']
        labels = {'name': 'Account Name: ', 'type': 'Account Type'}
