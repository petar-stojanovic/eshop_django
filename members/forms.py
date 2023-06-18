from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control fw-bold", "placeholder": "Email Address"}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={"class": "form-control fw-bold", "placeholder": "First Name", "autofocus": True}))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(
                                    attrs={"class": "form-control fw-bold", "placeholder": "Last Name"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control fw-bold"
        self.fields['username'].widget.attrs['placeholder'] = "Username"

        self.fields['password1'].widget.attrs['class'] = "form-control fw-bold"
        self.fields['password1'].widget.attrs['placeholder'] = "Password"

        self.fields['password2'].widget.attrs['class'] = "form-control fw-bold"
        self.fields['password2'].widget.attrs['placeholder'] = "Confirm Password"
        self.fields['password2'].label = "Confirm Password"

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please use a different email.")
        return email
