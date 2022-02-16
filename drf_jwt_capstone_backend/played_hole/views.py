from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import PlayedHole
from .serializers import PlayedHoleSerializer
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_played_holes(request):
    played_holes = PlayedHole.objects.all()
    serializer = PlayedHoleSerializer(played_holes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_played_hole(request):
    if request.method == 'POST':
        serializer = PlayedHoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET']) 
@permission_classes([IsAuthenticated])   
def get_played_hole_by_user(request):
    if request.method == 'GET':
        played_holes = PlayedHole.objects.filter(user_id=request.user.id)
        serializer = PlayedHoleSerializer(played_holes, many=True)
        return Response(serializer.data)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_played_hole(request, played_hole_id ):
    if request.method == 'PUT':
        played_hole = PlayedHole.objects.get(id=played_hole_id)
        serializer = PlayedHoleSerializer(played_hole, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_played_hole(request, played_hole_id):
    if request.method == 'DELETE':
        played_hole = PlayedHole.objects.get(id=played_hole_id)
        played_hole.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_hole_by_date(request, dt, course_id):
    if request.method == 'GET':
        # // convert the string dt into a date object
        # cvtDate = ???? "2022-02-16"
        played_hole = PlayedHole.objects.filter(course=course_id).filter(date=dt).aggregate(Sum('strokes'))
        # serializer = PlayedHoleSerializer(played_hole, many=True)
        return Response(played_hole)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_total_putts(request, dt, course_id):
    if request.method == 'GET':
        played_hole = PlayedHole.objects.filter(course=course_id).filter(date=dt).aggregate(Sum('putts'))
        return Response(played_hole)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_dates(request, course_id):
    if request.method =='GET':
        played_hole = PlayedHole.objects.filter(course=course_id).values('date').annotate(Sum('strokes'), Sum('putts'))
        return Response(played_hole)
    
    