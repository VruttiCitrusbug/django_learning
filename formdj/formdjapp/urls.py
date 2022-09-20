from . import views
from django.urls import path

urlpatterns = [
   path('',views.signup.as_view(),name="formlog")
]
