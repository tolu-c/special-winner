from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return f'my_files/{instance.user.username}/{filename}'
    
class PrivateFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self) -> str:
        return self.file.name