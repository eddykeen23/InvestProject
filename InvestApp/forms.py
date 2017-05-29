from django import forms

from .models import etf

class etf_form(forms.ModelForm):
    class Meta:
        model = etf
        fields = ['symbol', 'name']
        labels = {'symbol': 'Symbol:', 'name': 'Name:'}
