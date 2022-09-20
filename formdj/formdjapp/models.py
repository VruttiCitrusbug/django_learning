from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
class UserManager(BaseUserManager):
    use_in_migrations=True
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("email is require")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None,**extra_fields):
        # if not email:
        #     raise ValueError("email is require")
        # email=self.normalize_email(email)
        # user=self.model(email=email,**extra_fields)
        # user.set_password(password)
        # user.save(using=self._db)
        # return user
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Must is_staff True')
        return self.create_user(email,password,**extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    username=None
    email=models.EmailField(max_length=60,blank=False,unique=True)
    phno=models.IntegerField(max_length=10,blank=True,null=True)
    # last_login_time=models.DateTimeField(null=True,blank=True)
    # last_logout_time=models.DateTimeField(null=True,blank=True)
    name=models.CharField(max_length=100)
    USERNAME_FIELD='email'
    is_superuser= models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    REQUIRED_FIELDS = []
    objects =UserManager()