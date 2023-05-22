from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('', views.home, name='home'),
    path('files/', views.file_list, name='file_list'),
    path('files/<int:file_id>', views.file_detail, name='file_detail'),
    path('upload/', views.file_upload, name='file_upload'),
    path('accounts/login/', views.user_login, name="login"),
    path('accounts/register/', views.user_register, name="register"),
    path('logout/', views.user_logout, name='logout')
]
