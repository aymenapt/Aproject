from django.shortcuts import render
from rest_framework import generics 
from.models import Challenges , Images, Paragraph, Task, Titel 
from.serializers import ChallengesSreilalizer, ImagesSreilalizer, ParagraphSreilalizer ,TaskSreilalizer, TitelSreilalizer

# Create your views here.
class CreateTitels(generics.ListCreateAPIView):
     queryset=Titel.objects.all()
     serializer_class= TitelSreilalizer



class CreateImages(generics.ListCreateAPIView):
     queryset=Paragraph.objects.all()
     serializer_class= ImagesSreilalizer     



class CreateParagrahe(generics.ListCreateAPIView):
     queryset=Images.objects.all()
     serializer_class= ParagraphSreilalizer


class CreateTasks(generics.ListCreateAPIView):
     queryset=Task.objects.all()
     serializer_class= TaskSreilalizer


class CreateChallenges(generics.ListCreateAPIView):
     queryset=Challenges.objects.all()
     serializer_class= ChallengesSreilalizer    



       