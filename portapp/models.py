from djongo import models

class port(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    subject = models.CharField(max_length=100)
    mesage = models.CharField(max_length=100)
    

# Create your models here.
