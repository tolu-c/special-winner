from django import forms
from .models import PrivateFile

class PrivateFileForm(forms.ModelForm):
    class Meta:
        model = PrivateFile
        fields = ('file',)