from django import forms

# from .models import user

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Pick a username",
        "class": 'form-control',
        "autocomplete": 'off',
        })
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Enter your email",
        "class": 'form-control',
        "autocomplete": 'off',
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Create a password",
        "class": 'form-control',
        "autocomplete": 'off',
        })
    )
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm your password",
        "class": 'form-control',
        "autocomplete": 'off',
        })
    )


####################
# Using ModelForm instead of Form
####################
# class UserForm(forms.ModelForm):
#     # confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

#     class Meta:
#         model = user
#         fields = ['name', 'email', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
#         labels = {
#             'name': 'Username',
#             'email': 'Email',
#             'password': 'Password',
#         }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password != confirm_password:
    #         raise forms.ValidationError("Passwords do not match.")
        