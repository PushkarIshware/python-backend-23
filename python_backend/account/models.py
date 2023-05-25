from django.db import models
from django import forms

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# I want to add custom fields like mobile number

# AbstractUser Model VS AbstractBaseUser Model
# https://testdriven.io/blog/django-custom-user-model/#:~:text=AbstractUser%20vs%20AbstractBaseUser,-The%20default%20user&text=AbstractUser%20%3A%20Use%20this%20option%20if,own%2C%20completely%20new%20user%20model.


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password, **extra_fields):

        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self , email, password ,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    '''
    If you want to check User model in shell please paste below lines and then use ORM inside shell
    from django.contrib.auth import get_user_model
    User = get_user_model()
    '''

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    email= models.EmailField(null=True, blank=True, max_length=50, unique=True)
    contact = models.CharField(max_length=20, unique=True, null=True, blank=True)
    contact_verified = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    otp = models.CharField(max_length=8, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    
    objects = UserManager()

