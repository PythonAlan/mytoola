#!/usr/bin/env python3
#antuor:Alan

from django import forms

class AddForm(forms.Form):
    price = forms.FloatField(label='price')
    weight = forms.FloatField(label='wiehgt')
    purchase_price = forms.FloatField(label='purchase price')


