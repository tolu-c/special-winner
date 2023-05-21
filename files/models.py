from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PrivateFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='my_files/')

    def __str__(self) -> str:
        return self.file.name