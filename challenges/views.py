from django.shortcuts import render
from rest_framework import generics 
from.models import Challenges , Images, Paragraph, Task, Titel 
from.serializers import ChallengesSreilalizer, ImagesSreilalizer, ParagraphSreilalizer ,TaskSreilalizer, TitelSreilalizer
from rest_framework.views import APIView , Response

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

class PlanifyChallenge(generics.RetrieveUpdateAPIView):
     queryset=Challenges.objects.all()
     serializer_class= ChallengesSreilalizer 


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
     
      



       