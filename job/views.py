from django.shortcuts import render
from rest_framework import generics 
from.models import *
from.serializers import *
from rest_framework.views import APIView , Response
from rest_framework import status
from rest_framework.decorators import api_view
from challenges.models import Challenges
from django.db.models import Q
# Create your views here.

class CreateJobOffer(generics.ListCreateAPIView):
     queryset=JobOffer.objects.all()
     serializer_class= JobOfferSerializer 


class GetPlanfiedJobChallenge(APIView):
     def get(self,request):
          challenge=Challenges.objects.filter( Q(is_planified=True) & Q(challenge_type="job"))
          serializer=ChallengesSreilalizer(challenge,many=True)
          
          return Response(serializer.data, status=status.HTTP_200_OK)
     
class GetNONPlanfiedJobChallenges(APIView):
     def get(self,request):
          challenge=Challenges.objects.filter( Q(is_planified=False) & Q(challenge_type="job"))
          serializer=ChallengesSreilalizer(challenge,many=True)
          
          return Response(serializer.data, status=status.HTTP_200_OK)        