from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'eg:abi@gmail.com'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Paswoord'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
#class PasswordReset(PasswordChangeForm):
 #   pass
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
         
        exclude = ('password',)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)  # Adjust max_length based on your needs
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)