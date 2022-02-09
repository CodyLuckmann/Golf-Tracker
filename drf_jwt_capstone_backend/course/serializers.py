from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'city', 'zip_code', 'nine_hole_par', 'eighteen_hole_par']