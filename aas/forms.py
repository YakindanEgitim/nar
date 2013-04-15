from django import forms
from django.forms.util import ErrorDict
from django.forms.forms import NON_FIELD_ERRORS
from django.contrib.auth.models import User


class BaseForm(forms.Form):
    def add_form_error(self, message):
        if not self._errors:
            self._errors = ErrorDict()
        if not NON_FIELD_ERRORS in self._errors:
            self._errors[NON_FIELD_ERRORS] = self.error_class()
        self._errors[NON_FIELD_ERRORS].append(message)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class LoginForm(BaseForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
