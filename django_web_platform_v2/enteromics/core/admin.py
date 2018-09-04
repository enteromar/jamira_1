from django.contrib import admin

# Register your models here.
from .models import Tool
from .models import Tool_request
from .models import Genomic_file
admin.site.register(Tool)
admin.site.register(Genomic_file)
#admin.site.register(Tool_request)
