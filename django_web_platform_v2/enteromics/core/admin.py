from django.contrib import admin

# Register your models here.
from .models import Tool
from .models import Tool_request
admin.site.register(Tool)
#admin.site.register(Tool_request)
