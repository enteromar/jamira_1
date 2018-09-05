from django.shortcuts import render
from django.http import HttpResponse
from core.forms import ToolRequestForm
from core.forms import ToolRequestModelForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the enteromics index.")


def upload(request):
    if request.method == 'POST':
        form = ToolRequestForm(request.POST)
        if form.is_valid():
            #form.save()



            #process and save uploaded file
            myfile = request.FILES['Genomic_file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)


            #Get selected_tool from form
            selected_tool = form.cleaned_data['tools']
            #get absolute genome file path
            filepath=fs.path(filename)



            #return redirect('home')
            return render(request, 'core/form_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
    else:
        form = ToolRequestForm()
    return render(request, 'core/form_upload.html', {
        'form': form
    })

def model_upload(request):
    if request.method == 'POST':
        form = ToolRequestModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('home')
    else:
        form = ToolRequestModelForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
