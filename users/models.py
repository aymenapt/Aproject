from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,password=password,
                          first_name=first_name, **other_fields)
      
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'),unique=True)
    username = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=40)
    point=models.IntegerField(null=True,blank=True,default=0)
    skills=models.CharField(max_length=255, blank=True,null=True)
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    otp=models.CharField(max_length=40,blank=True)
    is_verified=models.BooleanField(default=False)
    is_baned=models.BooleanField(default=False)
    interviewlink=models.CharField(max_length=800,null=True,blank=True)
    bancount=models.IntegerField(null=True,blank=True,default=0)
    baned_time=models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.username
    
    @property
    def my_PRF_image(self):

       if self.image :
          return self.image.url
       return ''
    class Meta:
        ordering = ('-point',)