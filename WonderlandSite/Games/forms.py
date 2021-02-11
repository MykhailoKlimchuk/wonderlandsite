from .models import Contact
from django.forms import ModelForm, TextInput, Textarea


class ContactUsForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": TextInput(attrs={
                "placeholder": "Your Name"
            }),
            "email": TextInput(attrs={
                "placeholder": "Your Email"
            }),
            "subject": TextInput(attrs={
                "placeholder": "Subject"
            }),
            "message": Textarea(attrs={
                "placeholder": "Message"
            })
        }