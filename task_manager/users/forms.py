from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class BaseUserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        label=_("Password"),
        widget=forms.PasswordInput,
        help_text=_("Your password must contain at least 3 characters.")
    )
    password_confirm = forms.CharField(
        required=False,
        label=_("Confirm Password"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password again for verification.")
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'username': _('Username'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'username': forms.TextInput(attrs={'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['password'].widget.attrs.pop('required', None)
        self.fields['password_confirm'].widget.attrs.pop('required', None)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if not password:
            self.add_error('password', _('Required field'))
        if not password_confirm:
            self.add_error('password_confirm', _('Required field'))
        if password and len(password) < 3:
            self.add_error('password_confirm', _("The entered password is too short. It must contain at least 3 characters."))
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', _("Passwords do not match."))
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class UserRegistrationForm(BaseUserForm):
    pass


class UserUpdateForm(BaseUserForm):
    pass
