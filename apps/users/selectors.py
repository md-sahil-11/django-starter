from rest_framework.authtoken.models import Token


def add_token_to_user_serializer_selector(data, user):
    token, _ = Token.objects.get_or_create(user=user)
    data['token'] = token.key
    return data
