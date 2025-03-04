from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Data
from phonenumber_field.modelfields import PhoneNumberField

class SignUp(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), label='')
    first_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), label='')
    last_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), label='')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUp, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class AddPerson(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), label='')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), label='')
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}), label='')
    phone = PhoneNumberField()
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}), label='')
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), label='')
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), label='')
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}), label='')
    
    class Meta:
        model = Data
        exclude = ("user",)