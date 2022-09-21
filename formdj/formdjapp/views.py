
from urllib import request
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetView
from django.views.generic.base import TemplateView
from .forms import userform
from .models import User
class signup(CreateView):
    template_name='formlog.html'
    model = User
    fields = ['email','password','name','phno']
    labels = {'email':'Email','password':'Password','name':'Name','phno':'Phone Number'}
    success_url='/all'
class all(ListView):
    template_name='alluser.html'
    model=User
    def get_queryset(self):
        qs=User.objects.all()
        return qs
# class delete()
class update(UpdateView):
    template_name='formlog.html'
    model = User
    fields = ['email','password','name','phno']
    labels = {'email':'Email','password':'Password','name':'Name','phno':'Phone Number'}
    success_url='/login'
class delete(DeleteView):
    model=User
    template_name='delete.html'
    success_url='/login'
class login(LoginView):
    template_name='login.html'
class signin(TemplateView):
    template_name='signin.html'
class logout(LogoutView):
    template_name='logout.html'
class changepass(PasswordChangeView):
    template_name='changepass.html'
    success_url='/logout'
class forget(PasswordResetView):
    template_name='forget.html'