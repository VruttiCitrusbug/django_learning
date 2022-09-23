
from . import views
from django.urls import path
# from django.contrib.auth import views as auth_views
urlpatterns = [
   path('',views.signup.as_view(),name="formlog"),
   path('all',views.all.as_view(),name="all"),
   path('delete/<pk>',views.delete.as_view(),name="delete"),
   path('update/<pk>',views.update.as_view(),name="update"),
   path('login',views.login,name="login"),
   path('signin/',views.signin.as_view(),name="signin"),
   path('logout',views.logout.as_view(),name="logout"),
   path('changepass',views.changepass.as_view(),name="changepass"),
   path('forget',views.forget,name="forget"),
   # path('change',views.change,name="change"),
   # path('password_reset',views.forget.as_view(),name="password_reset"),
   # path("password_reset_confirm", views.confirm.as_view(), name="password_reset_confirm"),
   # path('password_reset_confirm/<uidb64>/<token>/',views.confirm.as_view(),name="password_reset_confirm"),
   # path('done',views.done.as_view(),name="done")
]
