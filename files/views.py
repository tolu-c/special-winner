from django.shortcuts import render, redirect
from .models import PrivateFile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import PrivateFileForm
from django.http import FileResponse, HttpResponse
import mimetypes
import os

# Create your views here.


def home(request):
    return render(request, 'index.html')


@login_required
def file_list(request):
    files = PrivateFile.objects.filter(user=request.user)
    return render(request, 'file_list.html', {'files': files})


@login_required
def file_detail(request, file_id):
    file = PrivateFile.objects.get(id=file_id, user=request.user)

    file_path = file.file.path

    if os.path.exists(file_path):
        content_type, _ = mimetypes.guess_type(file_path)

        if content_type is None:
            response = HttpResponse(file.file.read())
        else:
            response = FileResponse(file.file, content_type=content_type)
        response['Content-Disposition'] = 'inline; filename=' + \
            os.path.basename(file_path)

        # return response
        return render(request, 'file_detail.html', {'file': file, 'response': response, 'content_type': content_type})
    else:
        return HttpResponse('File not found')


@login_required
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


def user_login(request):
    return LoginView.as_view(template_name="login.html")(request)


def user_logout(request):
    logout(request)
    return redirect('files:home')
