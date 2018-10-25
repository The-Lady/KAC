from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)

User = get_user_model()


class UserLogInForm(forms.Form):
    username = forms.CharField(label="Enter username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # THIS METHOD IS ALWAYS CALLED WHEN CLEANED_DATA IS CALLED IN VIEWS.PY
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user_qs = User.objects.filter(username=username)
            if user_qs.count() == 0:
                raise forms.ValidationError("The user does not exist")
            else:
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError("Incorrect password")
                if not user.is_active:
                    raise forms.ValidationError("This user is no longer active")

        return super(UserLogInForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(label='Email Address',widget = forms.TextInput(attrs={'class': 'form-control'}))
    email2 = forms.EmailField(label='Confirm Email',widget = forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'password2'

        ]

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Passwords Don't Match")

        if email != email2:
            raise forms.ValidationError("Emails Don't Match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This Email has already been registered")

        user_qs = User.objects.filter(username=username)
        if user_qs.exists():
            raise forms.ValidationError("This Username is taken!")

        return super(UserRegisterForm, self).clean(*args, **kwargs)