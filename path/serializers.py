from rest_framework import serializers
from challenges.models import Answer 
from challenges.serializers import TaskSreilalizer
from.models import *
# Create here serializers 


class UserSerializer(serializers.ModelSerializer):
     class Meta :
          model=NewUser
          fields=['id','email', 'username','point']


class AnswerGamifiedCoursSerializer(serializers.ModelSerializer):
     class Meta:
        model = Answer
        fields = ['answer','question','user','gamifiedcours','coursparticpate'] 


class ParticipateOnCoursSerializer(serializers.ModelSerializer):
     answers = AnswerGamifiedCoursSerializer(many=True,read_only=True)
     class Meta :
          model=GamifiedCoursParticipate
          fields=['id','participate_by','gamifiedcours','participate_result','answers']


class ParticipateOnCoursListSerializer(serializers.ModelSerializer):
     answers = AnswerGamifiedCoursSerializer(many=True,read_only=True)
     user_detail=UserSerializer(read_only=True,source='participate_by')
     class Meta :
          model=GamifiedCoursParticipate
          fields=['id','user_detail','participate_result','finaldate_participate','answers']          

class GamifiedCoursSerializer(serializers.ModelSerializer):
    coursparticipate=ParticipateOnCoursListSerializer(many=True,read_only=True)
    task=TaskSreilalizer(many=True,read_only=True)
    image_url = serializers.SerializerMethodField()
    def get_image_url(self, obj):
          if obj.image:
            return f"http://127.0.0.1:8000{obj.image.url}"
          return None
    class Meta :
        model= GamifiedCours
        fields=('id','name','image','image_url','descreption','learningpath','coursparticipate','task')



class LearningPathSerializer(serializers.ModelSerializer):
    gamifiedcours=GamifiedCoursSerializer(many=True,read_only=True)
    image_url = serializers.SerializerMethodField()
    def get_image_url(self, obj):
          if obj.image:
            return f"http://127.0.0.1:8000{obj.image.url}"
          return None
    class Meta :
        model= LearningPath
        fields=('id','name','image','image_url','created_by','gamifiedcours',)


