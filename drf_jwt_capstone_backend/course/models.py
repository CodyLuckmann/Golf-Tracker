from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    nine_hole_par = models.IntegerField()
    eighteen_hole_par = models.IntegerField()
    
# Create your models here.
