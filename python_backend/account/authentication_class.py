import jwt
from django.contrib.auth import get_user_model, authenticate
from rest_framework import authentication
from rest_framework import exceptions

User = get_user_model()

class CustomJWTTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # jwt_token = request.COOKIES.get('jwt')
        jwt_token = request.META['HTTP_AUTHORIZATION']
        if not jwt_token:
            return None
        try:
            payload = jwt.decode(jwt_token, 'secret', algorithms=['HS256'])
            user = authenticate(email=payload['email'], password=payload['password'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return (user, jwt_token)