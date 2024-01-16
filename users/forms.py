from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordResetForm, SetPasswordForm
from django.forms import HiddenInput

from catalog.forms import CrispyFormMixin
from users.models import User


class UserForm(CrispyFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class RegisterForm(CrispyFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForgotPasswordForm(PasswordResetForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({
    #             'class': 'form-control',
    #             'autocomplite': 'off'
    #         })
    pass


class UserSetNewPasswordForm(SetPasswordForm):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({
    #             'class': 'form-control',
    #             'autocomplete': 'off'
    #         })


class UserProfileForm(CrispyFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = HiddenInput()
