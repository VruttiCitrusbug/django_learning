from django import forms
from .models import User
import re
class userform(forms.ModelForm):
        class Meta:
            model = User
            fields = ['email','password','name','phno']
        def clean(self):
            cleaned_data = super().clean()
            valname=cleaned_data['name']
            valphno = cleaned_data['phno']
            valemail =cleaned_data['email']
            valpass =cleaned_data['password']
            if len(valname)<3:
                raise forms.ValidationError('enter more than 2 characters')
            if not re.match(r'^[A-Za-z]+$',valname):
                raise forms.ValidationError("only alphabelts are allowed")
            if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',valemail):
                raise forms.ValidationError("Enetr valid email address")
            if len(valphno)!=10:
                raise forms.ValidationError("phone number contain 10 characters")
            if not re.match(r'^[0-9]',valphno):
                raise forms.ValidationError("Enetr valid phonenumber")
            if len(valpass)<8:
                raise forms.ValidationError("password greater then 8 characeters")
            if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$',valpass):
                raise forms.ValidationError("password must contain special character, one Capital latter,and one numeric value")
            return self.cleaned_data
            # labels = {'email':'Email','password':'Password','name':'Name','phno':'Phone Number'}
            # super().__init__(*args,**kwargs)
            # cleaned_data = super().clean()
# class logPage(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email','password']
#     def clean(self):
#         cleaned_data = super().clean()
#         E = cleaned_data.get('email')
#         P = cleaned_data.get('password')
#         return self.cleaned_data