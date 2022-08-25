from django.db import models

# Create your models here.
class Matkul(models.Model):  
    id = models.CharField(max_length=50)  
    nama_matkul = models.CharField(max_length=150)    
    dosen = models.CharField(max_length=1000)
    sks = models.CharField(max_length=10)
    class Meta:  
        db_table = "matkul"  