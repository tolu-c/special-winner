from django.contrib import admin
from .models import PrivateFile

# Register your models here.

@admin.register(PrivateFile)
class PrivateFileAdmin(admin.ModelAdmin):
    list_display = ['file']