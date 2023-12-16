from django.db import models

# Create your models here.
class employe(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=30)
    designation=models.CharField(max_length=50)
    salary=models.CharField(max_length=30)
    
