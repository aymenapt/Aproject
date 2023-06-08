from django.shortcuts import get_object_or_404, render
from rest_framework import generics

from challenges.models import Question ,Answer
from.models import GamifiedCours,GamifiedCoursParticipate
from.serializers import *
from rest_framework.views import APIView , Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q
# Create your views here.

class CreateLearinigPath(generics.ListCreateAPIView):
     queryset=LearningPath.objects.all()
     serializer_class= LearningPathSerializer


class CreateGamifiedCours(generics.ListCreateAPIView):
     queryset=GamifiedCours.objects.all()
     serializer_class= GamifiedCoursSerializer  


class LearnPathUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearningPath.objects.all()
    serializer_class = LearningPathSerializer  
    lookup_field = 'id'   

class GamifiedCoursUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = GamifiedCours.objects.all()
    serializer_class = GamifiedCoursSerializer 
    lookup_field = 'id'   



class ParticipateOnGamifiedCoursView(generics.ListCreateAPIView):
    queryset = GamifiedCoursParticipate.objects.all()
    serializer_class = ParticipateOnCoursSerializer
      
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        participate_id = serializer.validated_data['participate_by'].id
     
        serializer.save()
        return Response({
                'message': 'You have successfully participated.',
                'data': serializer.data
            }, status=status.HTTP_200_OK)





class MyAnswerCours(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerGamifiedCoursSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        answer = serializer.validated_data['answer']
        question = serializer.validated_data['question']
        mychallenge = serializer.validated_data['gamifiedcours']
        
        participate = get_object_or_404(GamifiedCoursParticipate,Q(participate_by=user)&Q(gamifiedcours=mychallenge))
        
        current_question = get_object_or_404(Question, id=question.id)

        
        try:
             
             answer = Answer.objects.get(coursparticpate=participate.id, question=question.id)
             print(answer)
             return Response({
                  'message': 'You have already answered this',
                  'data': serializer.errors
                     }, status=status.HTTP_400_BAD_REQUEST)
        except Answer.DoesNotExist:
            
            if current_question.question_solution == answer:
               serializer.save()
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