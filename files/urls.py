from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'files'

urlpatterns = [
    path('files/', views.file_list, name='file_list'),
    path('upload/', views.file_upload, name='file_upload'),
    path('logout/', auth_views.LogoutView.as_view(next_page='file_list'), name='logout')
]