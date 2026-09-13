from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(
        label="Nom",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Votre nom",
            }
        ),
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "votre@email.com",
            }
        ),
    )

    subject = forms.CharField(
        label="Sujet",
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sujet de votre message",
            }
        ),
    )

    message = forms.CharField(
        label="Message",
        max_length=5000,
        required=True,
        widget=forms.Textarea(
            attrs={
                "rows": 7,
                "placeholder": "Votre message...",
            }
        ),
    )