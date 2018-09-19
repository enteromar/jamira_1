from django import forms
from core.models import Tool,Genomic_file,Document

class ToolRequestForm(forms.Form):
    #name = forms.CharField(max_length=100)
    tools = forms.ModelMultipleChoiceField(queryset=Tool.objects.all())
    #genomic_file = forms.FileField()
    # class Meta:
    #     model = Genomic_file
    #     fields = ('isolation_source','host','upload' )

class ToolRequestModelForm(forms.Form):
    #name = forms.CharField(max_length=100)
    tools = forms.ModelMultipleChoiceField(queryset=Tool.objects.all())
    #file = forms.FileField()

    # class Meta:
    #     model = Genomic_file
    #     fields = ('isolation_source','host','upload', )
