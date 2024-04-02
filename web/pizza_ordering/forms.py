from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pizza_type', 'comment']
        labels = {
            'pizza_type': 'Select your pizza type',
            'comment': 'Any special instructions?'
        }