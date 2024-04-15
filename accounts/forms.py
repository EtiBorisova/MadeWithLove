from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from MadeWithLove.accounts.models import MadeWithLoveUser, ProfileModel
from django import forms


class CreateProfile(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['user']



class MadeWithLoveUserCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MadeWithLoveUser
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit)
        profile = ProfileModel(email=self.cleaned_data['email'],
                               user=user)
        if commit:
            profile.save()


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus':True,
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current password',
                'placeholder': 'Password'
            }
        )
    )


