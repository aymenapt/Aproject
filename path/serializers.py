from rest_framework import serializers 
from challenges.serializers import TaskSreilalizer
from.models import *
# Create here serializers 


class GamifiedCoursSerializer(serializers.ModelSerializer):
    task=TaskSreilalizer(many=True,read_only=True)
    image_url = serializers.SerializerMethodField()
    def get_image_url(self, obj):
          if obj.image:
            return f"http://127.0.0.1:8000{obj.image.url}"
          return None
    class Meta :
        model= GamifiedCours
        fields=('id','name','image','image_url','descreption','learningpath','task')



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


