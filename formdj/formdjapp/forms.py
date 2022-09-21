from django.core import validators
from django import forms
from .models import User

def phone(val):
    if len(val)!=10:
        raise forms.ValidationError('Phone must contain 10 digits')
class userform(forms.ModelForm):
    class Meta:
        model = User
        name=forms.CharField(validators=[validators.MaxLengthValidator(50)])
        email=forms.EmailField()
        phno=forms.IntegerField(validators=[phone])
        fields = ['email','password','name','phno']
        labels = {'email':'Email','password':'Password','name':'Name','phno':'Phone Number'}
    # def clean_email(self):
    #     email = self.cleaned_data['contact_email']
    #     validator = RegexValidator("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
    #     validator(email)
    #     return email