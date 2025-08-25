from django.apps import AppConfig
from django import forms

class AsiantoursagencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'asiantoursagency'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print(f"Sending email to {self.cleaned_data['email']} with message {self.cleaned_data['message']}")