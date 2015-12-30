from django import forms

from .models import SignUp


class ContactForm(forms.Form):
    """docstring for ContactForm"""
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    """docstring for SignUpForm"""
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):  # Overides a email function to clean email data.
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extention = provider.split('.')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
