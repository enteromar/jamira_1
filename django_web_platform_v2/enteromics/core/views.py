from django.shortcuts import render
from django.http import HttpResponse
from core.forms import ToolRequestForm
from core.forms import ToolRequestModelForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from core.pipelines import AutomatizedTool
# Create your views here.



def index(request):
    #return HttpResponse("Hello, world. You're at the enteromics index.")
    return render(request, 'core/home.html')

def progress(request):
    return render(request, 'core/progress.html')


def upload(request):
    if request.method == 'POST':
        form = ToolRequestForm(request.POST)
        if form.is_valid():
            #form.save()

            request_id = "001"
            g_path = 'media/analysis_requests/' + request_id + '/'
            #process and save uploaded file
            myfile = request.FILES['Genomic_file']
            #fs = FileSystemStorage()
            #print("absolute path to the request:",settings.BASE_DIR+g_path)
            fs = FileSystemStorage(g_path)
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)


            #get absolute genome file path
            filepath=fs.path(filename)
            #Get selected_tools from form
            selected_tools = form.cleaned_data['tools']
            for i in selected_tools:
                tool = i.tool_name
                print(tool)
                #call Analysis
                job = AutomatizedTool(tool,filepath)
                job.start()


            #return redirect('home')
            return render(request, 'core/progress.html', {
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
