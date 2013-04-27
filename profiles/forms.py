# profiles/forms.py
from django import forms

from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ('avatar',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  )
