from django import forms
from .models import User

class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password','name','phno']
        labels = {'email':'Email','password':'Password','name':'Name','phno':'Phone Number'}