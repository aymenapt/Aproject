from django.shortcuts import get_object_or_404, render
from rest_framework import generics 
from.models import Challenges , Images, Paragraph, Task, Titel 
from.serializers import *
from rest_framework.views import APIView , Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q
# Create your views here.

class GetSposorAds(generics.ListCreateAPIView):
     queryset=SposorAds.objects.all()
     serializer_class= AdsSreilalizer



class CreateTitels(generics.ListCreateAPIView):
     queryset=Titel.objects.all()
     serializer_class= TitelSreilalizer

class TitelUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Titel.objects.all()
    serializer_class = UpdateTitelSreilalizer
    lookup_field = 'id'  

class CreateImages(generics.ListCreateAPIView):
     queryset=Paragraph.objects.all()
     serializer_class= ImagesSreilalizer     

class ImagesUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = UpdateImagesSreilalizer
    lookup_field = 'id' 

class CreateFile(generics.ListCreateAPIView):
     queryset=TaskFile.objects.all()
     serializer_class= TaskFileSreilalizer

class FileUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskFile.objects.all()
    serializer_class = UpdateFileSreilalizer
    lookup_field = 'id' 

class CreateParagrahe(generics.ListCreateAPIView):
     queryset=Paragraph.objects.all()
     serializer_class= ParagraphSreilalizer

class ParagrapheUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = UpdateParagraphSreilalizer
    lookup_field = 'id' 

class CreateQuestion(generics.ListCreateAPIView):
     queryset=Question.objects.all()
     serializer_class= QuestionSreilalizer

class QuestionUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = UpdateQuestionSreilalizer
    lookup_field = 'id' 

class CreateVideo(generics.ListCreateAPIView):
     queryset=Video.objects.all()
     serializer_class= VideoSreilalizer     

class VideoUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = UpdateVideoSreilalizer
    lookup_field = 'id' 

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
          challenge=Challenges.objects.filter( Q(is_planified=True) & Q(challenge_type="challenge"))
          serializer=ChallengesSreilalizer(challenge,many=True)
          
          return Response(serializer.data, status=status.HTTP_200_OK)
     
class GetNONPlanfiedchallenges(APIView):
     def get(self,request):
          challenge=Challenges.objects.filter( Q(is_planified=False) & Q(challenge_type="challenge"))
          serializer=ChallengesSreilalizer(challenge,many=True)
          
          return Response(serializer.data, status=status.HTTP_200_OK)   


class RegeitreOnChallenge(generics.ListCreateAPIView):
  
      queryset = Registre.objects.all()
      serializer_class = RegistreSerializer
    
      def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        challenge_id = serializer.validated_data['challenge'].id
        challenge = Challenges.objects.get(id=challenge_id)
        
        if timezone.now() < challenge.start_date:
            serializer.save()
            return Response({
                'message': 'You are registered',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'message': 'Registration not allowed for this challenge',
        }, status=status.HTTP_400_BAD_REQUEST)


class ParticipateOnChallenge(generics.ListCreateAPIView):
    queryset = Participate.objects.all()
    serializer_class = ParticipateSerializer
      
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        participate_id = serializer.validated_data['participate_by'].id
        
        if Registre.objects.filter(registre_by=participate_id).exists():
            serializer.save()
            return Response({
                'message': 'You have successfully participated.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            'message': 'You are not registered.',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    


class Answer(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        answer = serializer.validated_data['answer']
        question = serializer.validated_data['question']
        
        participate = get_object_or_404(Participate, participate_by=user)
        current_question = get_object_or_404(Question, id=question.id)
        
        if current_question.question_solution == answer:
            participate.participate_result += current_question.question_point
            participate.save()
            
            user.point += current_question.question_point
            user.save()
            
            return Response({
                'message': 'Correct answer',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            'message': 'Wrong answer',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
             



             









           
     
      



       