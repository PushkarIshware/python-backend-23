from django.urls import path
from account.views import *
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup', RegisterUser.as_view(), name='register-user'),
    path('signin', LoginUser.as_view(), name='login-user'),
    path('profile', Profile.as_view(), name='user-profile'),
    path('logout', LogoutUser.as_view(), name='logout'),
]