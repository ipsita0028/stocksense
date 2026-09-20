from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BootstrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class RegisterForm(BootstrapMixin, UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')


class LoginForm(BootstrapMixin, AuthenticationForm):
    pass