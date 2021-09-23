from django import forms

class User(forms.Form):
    name = forms.CharField()
    token = forms.CharField(required=False)

class Post(forms.Form):
    token = forms.CharField(required=False)