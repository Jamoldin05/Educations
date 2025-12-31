from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label="Ism",
        widget=forms.TextInput(attrs={
            'class': 'form-control border-top-0 border-right-0 border-left-0 p-0',
            'placeholder': 'Your Name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control border-top-0 border-right-0 border-left-0 p-0',
            'placeholder': 'Your Email',
            'required': 'required'
        })
    )
    message = forms.CharField(
        label="Xabar",
        widget=forms.Textarea(attrs={
            'class': 'form-control border-top-0 border-right-0 border-left-0 p-0',
            'rows': 5,
            'placeholder': 'Message',
            'required': 'required'
        })
    )
