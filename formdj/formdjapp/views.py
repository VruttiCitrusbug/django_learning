from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.views.generic.base import TemplateView
# from django.views.generic import View
from django.contrib.auth.models import auth
# from django.views.generic.edit import FormView
from .forms import loginf, userform
from .models import User
from django.shortcuts import render,redirect

# class signup(FormView):

#     template_name = 'formlog.html'
#     form_class = userform
#     success_url = '/all'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

class signup(CreateView):
    template_name='formlog.html'
    model = User
    form_class=userform
    # fields = ['email','password','name','phno']
    # labels = {'email':'Email','password':'Password','name':'Name','phno':'Phone Number'}
    def form_valid(self, form):
        form.clean()
        return super().form_valid(form)
    # template_name='formlog.html'
    success_url='/all'
#     if form.is_valid():
#         pass
    
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
# class login(LoginView):
#     template_name='login.html'
#     success_url='signin'
def login(request):
    if request.method  == 'POST':
        form = loginf(request.POST)
        if form.is_valid():
            email =  form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(email)
            user=auth.authenticate(email=email,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('signin/')
            else:
                return HttpResponse("invalid data")
    return render(request,'login.html',{'form':loginf})
# def login(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')

#         user=auth.authenticate(email=email,password=password)
#         print(email)
#         if user is not None:
#             auth.login(request,user)
#             return redirect(request,'signin.html')
#         else:
#             return HttpResponse("invalid data")
#     return render(request,'login.html')
class signin(TemplateView):
    template_name='signin.html'
class logout(LogoutView):
    template_name='logout.html'
class changepass(PasswordChangeView):
    template_name='changepass.html'
    success_url='/logout'
# class forget(PasswordResetView):
#     template_name='forget.html'
#     success_url='/change'
# class change(PasswordResetDoneView):
#     template_name='change.html'
#     success_url='/confirm'
# class confirm(PasswordResetConfirmView):
#     template_name='confirm.html'
#     success_url='/done'
# class done(PasswordResetCompleteView):
#     template_name='done.html'
#     success_url='/login'