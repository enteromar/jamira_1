from django import forms
from core.models import Tool

class ToolRequestForm(forms.Form):
    name = forms.CharField(max_length=100)
    tools = forms.ModelMultipleChoiceField(queryset=Tool.objects.all())
