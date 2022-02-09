from rest_framework import serializers
from .models import PlayedHole

class PlayedHoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayedHole
        fields = ['id', 'user_id', 'course', 'date', 'hole', 'par', 'strokes', 'putts', 'driver_distance', 'fairway']