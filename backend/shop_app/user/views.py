from rest_framework.viewsets import ModelViewSet
from ..models import User
from .serializers import UserListSerializer, RegisterSerializer, UserSerializer
from ..permissions import IsNotAuthenticated, IsAdmin, IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsNotAuthenticated]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        else:
            return UserSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action in ['destroy', 'list', 'create']:
            self.permission_classes = [IsAuthenticated, IsAdmin]
        return super(self.__class__, self).get_permissions()
