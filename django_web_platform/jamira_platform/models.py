from django.db import models

# Create your models here.

class  Genomic_file(models.Model):
    """docstring for Genomic_file."""
    id_genomic_file = models.AutoField(primary_key=True)
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
    id_tool = models.AutoField(primary_key=True)
    path=models.FilePathField()
    tool_name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    tp_tool=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    """docstring for User."""
    id_user = models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    institution=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    is_super_user= models.BooleanField()

    def __str__(self):
        return self.full_name

class Tool_request(models.Model):
    """docstring for Tool_request"""
    id_request = models.IntegerField(primary_key=True)

    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    verbose_name="the user",
    )


    selected_tool = models.ForeignKey(
    Tool,
    on_delete=models.CASCADE,
    verbose_name="the analysis selected tool by user",
    )

    input_file = models.ForeignKey(
    Genomic_file,
    on_delete=models.CASCADE,
    verbose_name="the uploaded genomic file by user",
    )

    def __str__(self):
        return self.id_request
