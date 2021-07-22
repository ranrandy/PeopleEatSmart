from django import forms

class SignUpForm(forms.Form):
    UserName = forms.CharField(label='UserName', max_length=100)
    Password = forms.CharField(label='Password', max_length=100)