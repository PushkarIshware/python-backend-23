from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
import jwt
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from .authentication_class import CustomJWTTokenAuthentication


from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your views here.
class RegisterUser(APIView):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('login-user')
        else:
            messages.error(request, "User exists")
            return render(request, "signup.html")

class LoginUser(APIView):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        User = get_user_model()
        email = request.data['email']
        password = request.data['password']

        user = authenticate(email=email, password=password)
        
        if user and user.is_active:
            print("INSIDE IF USER")
            payload = {'email': email, 'password': password}
            
            jwt_token = jwt.encode(payload, "secret", algorithm='HS256').decode('utf-8')

            print(jwt_token)
            # response = Response()

            # response = redirect('home')
            # response.set_cookie(key='jwt', value=jwt_token, httponly=True)
            return JsonResponse({"jwt_token": jwt_token})
        
        else:
            return render(request, 'login.html')


class Home(APIView):

    authentication_classes = [CustomJWTTokenAuthentication]

    def get(self, request):
        return render(request, 'index.html')
    

class LogoutUser(APIView):

    authentication_classes = [CustomJWTTokenAuthentication]

    def get(self, request):
        return redirect(request, 'home')
    

class Profile(APIView):

    authentication_classes = [CustomJWTTokenAuthentication]

    def get(self, request):
        return render(request, 'profile.html')