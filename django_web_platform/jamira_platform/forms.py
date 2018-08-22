from django import forms

from uploads.core.models import Genomic_file


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Genomic_file
        fields = ('description', 'document', )
