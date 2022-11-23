from django.conf import settings

from rest_framework import serializers

from apps.users.models import User
from apps.users.selectors import add_token_to_user_serializer_selector


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "created_at",
        )
        read_only_fields = (
            "created_at",
        )
    
    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        data = add_token_to_user_serializer_selector(data, instance)
        return data