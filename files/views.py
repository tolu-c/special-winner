from django.shortcuts import render, redirect
from .models import PrivateFile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import PrivateFileForm

# Create your views here.

# @login_required
def file_list(request):
    files = PrivateFile.objects.filter(user=request.user)
    return render(request, 'file_list.html', {'files': files})

# @login_required
def file_upload(request):
    if request.method == 'POST':
        form = PrivateFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            return redirect('files:file_list')
    else:
        form = PrivateFileForm()
    return render(request, 'file_upload.html', {'form': form})