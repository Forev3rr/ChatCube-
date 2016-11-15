from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status, views
from django.contrib.auth import authenticate, login, logout
import json
from .models import User, Group, CustomUser
from .permissions import IsAccountOwner
from .serializers import UserSerializer, GroupSerializer, CustomUserSerializer


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class LoginView(views.APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        account = authenticate(username=username, password=password)
        if account is not None:
            if account.is_active:
                login(request, account)
                serialized = CustomUserSerializer(account)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)

class CustomUserViewSet(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            CustomUser.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     # return User.objects.filter(project__party__customuser=user)
    #     return User.objects.filter(project__party__customuser=user)

class GroupViewSet(viewsets.ModelViewSet):
    model = Group
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
