#!/usr/bin/env python3
#antuor:Alan

from django import forms

class AddForm(forms.Form):
    price = forms.FloatField(label='输入外币售价') #售价
    weight = forms.IntegerField(label='输入重量g')
    purchase_price = forms.FloatField(label='输入采购价¥') #采购价
    volume = forms.FloatField(label='输入体积m³',initial=0.001,required=False)

