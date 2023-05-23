from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'api'

urlpatterns = [
    path('', views.getRoutes, name='get_routes'),
    path('files/', views.get_files, name='get_files'),
    path('files/<str:file_id>/', views.get_file, name='get_file'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.user_register, name='register')
]
