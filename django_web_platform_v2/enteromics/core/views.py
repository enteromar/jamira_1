from django.shortcuts import render
from django.http import HttpResponse
from core.forms import ToolRequestForm
# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the enteromics index.")


def upload(request):
    if request.method == 'POST':
        form = ToolRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('home')
    else:
        form = ToolRequestForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
