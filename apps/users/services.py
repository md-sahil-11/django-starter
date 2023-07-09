from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from apps.users.models import User


def login_user_service(email, password):
    user = authenticate(email=email, password=password)
    return user
    

def register_user_service(email, password, name):
    user = User.objects.create(email=email, name=name)
    user.set_password(password)
    user.save()
    
    return user


def logout_user_service(user):
    Token.objects.filter(user=user).delete()


def add_token_to_user_serializer_selector(data, user):
    token, _ = Token.objects.get_or_create(user=user)
    data['token'] = token.key
    return data
