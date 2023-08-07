from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter Email", "required": "True", 'class': 'form-control'}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password", 'class': 'form-control'}
        ),
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise ValidationError('Invalid email or password')
        return cleaned_data


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter Email", "required": "True", 'class': 'form-control'}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password", 'class': 'form-control'}
        ),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password", 'class': 'form-control'}), label="Confirm Password"
    )
    role = forms.ChoiceField(
        choices=[("0", "Visitor"), ("1", "Librarian")],
        widget=forms.Select(attrs={'class': 'form-select'}),
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        return cleaned_data
