from django import forms

class Contact(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required= True)
    phone = forms.CharField(min_length=11, max_length=11, required=True)
    msg = forms.CharField(max_length=1500, required=True)