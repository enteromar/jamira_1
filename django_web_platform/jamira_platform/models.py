from django.db import models

# Create your models here.

class  Genomic_file(models.Model):
    """docstring for Genomic_file."""
    filename = models.CharField(max_length=200)
    upload = models.FileField(upload_to='uploads/')
    tp_file = models.CharField(max_length=5)
    tax_id = models.CharField(max_length=30, blank=True)
    host = models.CharField(max_length=50, blank=True)
    isolation_source = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.filename
class Tool(models.Model):
    """docstring for Tool."""
    path=models.FilePathField()
    tool_name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    tp_tool=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class User(object):
    """docstring for User."""
    full_name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    institution=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    is_super_user= models.BooleanField()
