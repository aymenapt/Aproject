from django.shortcuts import render
from rest_framework import generics 
from.models import *
from.serializers import *
from rest_framework.views import APIView , Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

class CreateLearinigPath(generics.ListCreateAPIView):
     queryset=LearningPath.objects.all()
     serializer_class= LearningPathSerializer


class CreateGamifiedCours(generics.ListCreateAPIView):
     queryset=GamifiedCours.objects.all()
     serializer_class= GamifiedCoursSerializer  