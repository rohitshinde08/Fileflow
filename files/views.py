from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
from .models import File
from .forms import FileUploadForm

# Upload View
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

# List Files View
def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {'files': files})

# Download View
def download_file(request, file_id):
    file_obj = get_object_or_404(File, id=file_id)
    response = FileResponse(file_obj.file.open('rb'), as_attachment=True, filename=file_obj.filename)
    return response
