from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username', 'email', 'phone', 'user_type'
        ]

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'user_type': 'User Type',
            'password': 'Password',
            'confirm_password': 'Confirm Password',
        }

        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'
        
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholders.get(field_name, '')
            })


    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get ('password')
        p2 = cleaned_data.get('confirm_password')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(label="Username or User ID", 
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Enter username or user ID'
                                   }))
    password = forms.CharField( 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
            }))
