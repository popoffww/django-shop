from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()

    name.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control', 'type': 'password'})
    confirm_password.widget.attrs.update({'class': 'form-control', 'type': 'password'})

    class Meta:
        model = Subscriber
        fields = ('name','email', 'password', 'confirm_password')
