from django import forms


class UserBioForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(label='Your age')
    bio = forms.CharField(label='Biography', widget=forms.Textarea)