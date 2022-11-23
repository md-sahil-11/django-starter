
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.users.api.serializers import UserSerializer
from apps.users.models import User
from apps.users.services import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(
        detail=False,
        methods=["POST"],
        permission_classes=(permissions.AllowAny,),
    )
    def login(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = login_user_service(email, password)
        if not user:
            return Response({"success": False, "err": "Invalid password or email!"})
        
        return Response({"success": True, 
            "data": self.serializer_class(user).data
        }, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["POST"],
        permission_classes=(permissions.IsAuthenticated,),
    )
    def logout(self, request, *args, **kwargs):
        logout_user_service(request.user)
        return Response({"success": True}, status=status.HTTP_200_OK)
    
    @action(
        detail=False,
        methods=["POST"],
        permission_classes=(permissions.AllowAny,),
    )
    def register(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        name = request.data.get("name")

        user = register_user_service(email, password, name)
        if not user:
            return Response({"success": False, "err": "Invalid password or email!"})
        
        return Response({"success": True, 
            "data": self.serializer_class(user).data
        }, status=status.HTTP_201_CREATED)