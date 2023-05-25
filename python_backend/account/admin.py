from django.contrib import admin

# Register your models here.

from .models import User
from rest_framework.authtoken.models import Token

admin.site.register(User)