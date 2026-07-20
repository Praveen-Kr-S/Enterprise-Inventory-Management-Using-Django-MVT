from django.forms import ModelForm
from .models import Customer
import django.forms as forms

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_since']

        widgets = {
            'customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'customer_since': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }