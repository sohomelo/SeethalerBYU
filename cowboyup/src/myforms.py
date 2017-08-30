from django import forms

class MyForm(forms.Form):
    org = forms.CharField(label='GIT Organization', max_length=100)
    username = forms.CharField(label='GIT Organization User Name', max_length=100)
    password = forms.CharField(label='Password', max_length=100)