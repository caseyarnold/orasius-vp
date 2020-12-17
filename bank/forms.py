from django import forms
from .models import BankAccount

class BankForm(forms.Form):
    type = forms.ChoiceField( [('withdraw','Withdraw'),('deposit','Deposit')], required=True, label='')
    cp = forms.IntegerField(required=True, label='')
