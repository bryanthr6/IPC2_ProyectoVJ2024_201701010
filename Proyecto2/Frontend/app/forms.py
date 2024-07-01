from django import forms

class LoginForm(forms.Form):
    iduser = forms.CharField(label='iduser', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label='password', max_length=100)

class FileForm(forms.Form):
    file = forms.FileField(label='file')
