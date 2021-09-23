from django import forms

class Country(forms.Form):
    country = forms.CharField()

class Tweet(forms.Form):
    tweet = forms.CharField()