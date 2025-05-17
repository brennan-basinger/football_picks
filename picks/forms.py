# picks/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Assuming you're using a custom User model from your app

class CustomUserCreationForm(UserCreationForm):
    terms_agreed = forms.BooleanField(
        required=True,
        label="I agree to the Terms and Conditions"
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password1',
            'password2',
        )

    def clean_terms_agreed(self):
        # Optional explicit check in case someone tries to manipulate POST data
        terms_agreed = self.cleaned_data.get('terms_agreed')
        if not terms_agreed:
            raise forms.ValidationError("You must agree to the Terms and Conditions to register.")
        return terms_agreed
