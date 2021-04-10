from django.db import models

# Create your models here.
class Player(models.Model):
    pno=models.IntegerField()
    pname=models.CharField(max_length=64)
    pruns=models.IntegerField()
    pfours=models.IntegerField()
    psixes=models.IntegerField()
