from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CommentForm(forms.Form):
    name = forms.CharField(
        max_length =60,
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Name"
        })
    )
    email = forms.EmailField(
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Email"
        })
    )
    body = forms.CharField(
        widget= forms.Textarea(
            attrs={
                "class" :"form-control",
                "placeholder":"Leave a comment!"
            })
    )


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length =60,
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Name"
        })
    )
    email = forms.EmailField(
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Email"
        })
    )
    phone = PhoneNumberField(
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Phone Number"
        })
    )
    message = forms.CharField(
        widget= forms.Textarea(
            attrs={
                "class" :"form-control",
                "placeholder":"Leave a message!"
            })
    )
