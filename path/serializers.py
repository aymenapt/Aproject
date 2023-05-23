from rest_framework import serializers 
from challenges.serializers import TaskSreilalizer
from.models import *
# Create here serializers 


class GamifiedCoursSerializer(serializers.ModelSerializer):
    task=TaskSreilalizer(many=True,read_only=True)
    class Meta :
        model= GamifiedCours
        fields=('id','name','image','descreption','learningpath','task')



class LearningPathSerializer(serializers.ModelSerializer):
    gamifiedcours=GamifiedCoursSerializer(many=True,read_only=True)
    class Meta :
        model= LearningPath
        fields=('id','name','image','gamifiedcours',)


