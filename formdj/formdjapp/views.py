from django.views.generic.base import TemplateView
from .forms import userform
from .models import User
class signup(TemplateView):
    template_name='formlog.html'
    def get_context_data(self,*args, **kwargs):
        # contex=super().get_context_data(**kwargs)
        form=userform()
        return {'form':form}