from .models import Contact
from django.forms import ModelForm, TextInput, Textarea


class ContactUsForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": TextInput(attrs={
                "placeholder": "Your Name",
                "class": "form-control"
            }),
            "email": TextInput(attrs={
                "placeholder": "Your Email",
                "class": "form-control"

            }),
            "subject": TextInput(attrs={
                "placeholder": "Subject",
                "class": "form-control"
            }),
            "message": Textarea(attrs={
                "placeholder": "Message",
                "class": "form-control md-textarea",
                "rows": 6
            })
        }