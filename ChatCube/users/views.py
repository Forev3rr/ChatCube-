from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status, views
from django.contrib.auth import authenticate, login, logout
import json
from .models import Group, CustomUser
from .serializers import GroupSerializer, CustomUserSerializer
from django.shortcuts import render


class LogoutView(views.APIView):
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


def index(request):
    return render(request, 'users/home.html')


def contact(request):
    return render(request, 'users/basic.html', {'content':[request.user.username, request.user.email]})


# def register(request):
#     form = RegisterForm()
#     if request.method == "POST":
#         form = RegisterForm(request.POST) #if no files
#         if form.is_valid():
#             #do something if form is valid
#     context = {
#         'form': form
#     }
#     return render(request, "template.html", context)

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         user = CustomUser(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})


class CustomUserViewSet(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            CustomUser.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    model = Group
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
