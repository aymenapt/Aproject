from rest_framework import serializers 
from.models import *


class AdsSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=SposorAds
         fields="__all__"

class ParagraphSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Paragraph
         fields= "__all__"

class ImagesSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Images
         fields="__all__"

class TitelSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Titel
         fields="__all__"


class TaskSreilalizer(serializers.ModelSerializer):
     images=ImagesSreilalizer(many=True,read_only=True)
     titel=TitelSreilalizer(many=True,read_only=True)
     paragraph=ParagraphSreilalizer(many=True,read_only=True)
     
     class Meta :
         model=Task
         fields="__all__"

class ChallengeRulesSerializer(serializers.ModelSerializer):
     class Meta :
         model=ChallengeRules
         fields="__all__"
              

class ChallengesSreilalizer(serializers.ModelSerializer):
        task=TaskSreilalizer(many=True)
        challengerule=ChallengeRulesSerializer(many=True)
        class Meta :
           model=Challenges
           fields=('id','name','image','descreption','start_date','end_date','points','is_planified','max_teamsize','challengerule','task')



class PlanifyChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenges
        fields = ['name', 'descreption', 'points', 'start_date', 'end_date','is_planified']
        extra_kwargs = {
            'name': {'required': False},
            'descreption': {'required': False},
            'points': {'required': False},
            'start_date': {'required': True},
            'end_date': {'required': True},
            'is_planified': {'required': False}
        }       