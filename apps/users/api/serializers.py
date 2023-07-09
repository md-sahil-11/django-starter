from django.conf import settings

from rest_framework import serializers

from apps.users.models import User


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
    
    