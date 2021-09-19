from django import forms


# creating a form
class InputForm(forms.Form):
    to = forms.CharField(max_length=200)
    data = forms.CharField(max_length=1000)
