from django.shortcuts import render, redirect
from .models import PrivateFile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import PrivateFileSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ObtainJWTTokenView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def file_list(request):
    files = PrivateFile.objects.filter(user=request.user)
    serializer = PrivateFileSerializer(files, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def file_detail(request, file_id):
    try:
        file = PrivateFile.objects.get(id=file_id, user=request.user)
        serializer = PrivateFileSerializer(file)
        return Response(serializer.data)
    except PrivateFile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def file_upload(request):
    serializer = PrivateFileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_login(request):
    return LoginView.as_view(template_name="login.html")(request)


def user_logout(request):
    logout(request)
    return redirect('files:home')


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('files:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
