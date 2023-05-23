from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'files'

urlpatterns = [
    # path('', views.home, name='home'),
    path('files/', views.file_list, name='file_list'),
    path('files/<int:file_id>', views.file_detail, name='file_detail'),
    path('upload/', views.PrivateFileUploadView.as_view(), name='file_upload'),
    path('register/', views.UserRegistrationView.as_view(), name="register"),
    # path('token/', views.ObtainJWTTokenView.as_view(), name="obtain_token"),
    path('login/', views.UserLoginView.as_view(), name='login')
]
