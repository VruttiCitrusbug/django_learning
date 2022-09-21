from unicodedata import name
from . import views
from django.urls import path
# from django.contrib.auth import views as auth_views
urlpatterns = [
   path('',views.signup.as_view(),name="formlog"),
   path('all',views.all.as_view(),name="all"),
   path('delete/<pk>',views.delete.as_view(),name="delete"),
   path('update/<pk>',views.update.as_view(),name="update"),
   path('login',views.login.as_view(),name="login"),
   path('signin/',views.signin.as_view(),name="signin"),
   path('logout',views.logout.as_view(),name="logout"),
   path('changepass',views.changepass.as_view(),name="changepass"),
   # path('forget',views.forget.as_view(),name="forget")
]
