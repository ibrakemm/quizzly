from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class signUp(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="password",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="confirm password",
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") !=cleaned_data.get("confirm_password"):
            raise forms.ValidationError("passwords do not match")
        return cleaned_data
        
class Login(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="password",
    )