from django.shortcuts import render
from rest_framework import generics 
from.models import Challenges , Images, Paragraph, Task, Titel 
from.serializers import *
from rest_framework.views import APIView , Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

class GetSposorAds(generics.ListCreateAPIView):
     queryset=SposorAds.objects.all()
     serializer_class= AdsSreilalizer



class CreateTitels(generics.ListCreateAPIView):
     queryset=Titel.objects.all()
     serializer_class= TitelSreilalizer



class CreateImages(generics.ListCreateAPIView):
     queryset=Paragraph.objects.all()
     serializer_class= ImagesSreilalizer     

class CreateFile(generics.ListCreateAPIView):
     queryset=TaskFile.objects.all()
     serializer_class= TaskFileSreilalizer

class CreateParagrahe(generics.ListCreateAPIView):
     queryset=Paragraph.objects.all()
     serializer_class= ParagraphSreilalizer

class CreateQuestion(generics.ListCreateAPIView):
     queryset=Question.objects.all()
     serializer_class= QuestionSreilalizer

class CreateVideo(generics.ListCreateAPIView):
     queryset=Video.objects.all()
     serializer_class= VideoSreilalizer     

class CreateTasks(generics.ListCreateAPIView):
     queryset=Task.objects.all()
     serializer_class= TaskSreilalizer


class CreateChallegeRules(generics.ListCreateAPIView):
     queryset=ChallengeRules.objects.all()
     serializer_class= ChallengeRulesSerializer


class CreateChallenges(generics.ListCreateAPIView):
     queryset=Challenges.objects.all()
     serializer_class= ChallengesSreilalizer    
"""

class PlanifyChallenge(generics.RetrieveUpdateAPIView):
     queryset=Challenges.objects.all()
     serializer_class= ChallengesSreilalizer 

"""


class PlanifyChallenge(APIView):
    def put(self, request, challenge_id):
        challenge = Challenges.objects.get(id=challenge_id)
        serializer = PlanifyChallengeSerializer(challenge,data=request.data)

        if serializer.is_valid():
            start_date = serializer.validated_data.get('start_date')
            end_date = serializer.validated_data.get('end_date')
            challenge.start_date = start_date
            challenge.end_date = end_date
            challenge.is_planified=True
            challenge.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPlanfiedchallenges(APIView):
     def get(self,request):
          challenge=Challenges.objects.filter(is_planified=True)
          serializer=ChallengesSreilalizer(challenge,many=True)
          
          return Response(serializer.data, status=status.HTTP_200_OK)
     
class GetNONPlanfiedchallenges(APIView):
     def get(self,request):
          challenge=Challenges.objects.filter(is_planified= False)
          serializer=ChallengesSreilalizer(challenge,many=True)
          
          return Response(serializer.data, status=status.HTTP_200_OK)   


class RegeitreOnChallenge(generics.ListCreateAPIView):
     queryset=Registre.objects.all()
     serializer_class= RegistreSerializer  

"""""
class PlanifyChallenge(APIView):
    def put(self, request, pk):
        challenge = Challenges.objects.get(id=pk)
        serializer = PlanifyChallengeSerializer(challenge, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 200,
                'message': 'Challenge start and end dates updated successfully',
                'data': serializer.data
            })
        return Response({
            'status': 400,
            'message': 'Invalid input',
            'data': serializer.errors
        })
          
"""""
     
      



       