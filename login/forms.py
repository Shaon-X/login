from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class register_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  #built-in names

    def __init__(self, *args, **kwargs):
        super(register_form, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        #self.fields['password1'].required = False
        #self.fields['password2'].required = False
