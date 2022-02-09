from django.db import models
from django.contrib.auth import get_user_model
from django.apps import apps
from course.models import Course

User = get_user_model()


# Create your models here.
class PlayedHole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    hole = models.IntegerField()
    par = models.IntegerField()
    strokes = models.IntegerField()
    putts = models.IntegerField()
    driver_distance = models.IntegerField(null=True)
    fairway = models.BooleanField()
    