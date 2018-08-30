from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from jamira.jamira_platform.models import Genomic_file
from uploads.core.forms import DocumentForm
# Create your views here.




def home(request):
    documents = Genomic_file.objects.all()
    return render(request, 'jamira_platform/home.html', { 'documents': documents })


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'jamira_platform/model_form_upload.html', {
        'form': form
    })
