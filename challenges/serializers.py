from django.conf import settings
from rest_framework import serializers 
from.models import *
from users.models import NewUser


class UserSerializer(serializers.ModelSerializer):
     class Meta :
          model=NewUser
          fields=['id','email', 'username']
     


class RegistreSerializer(serializers.ModelSerializer):
     class Meta :
          model=Registre
          fields=['id','registre_by','challenge']



class RegistreListSerializer(serializers.ModelSerializer):
     user_detail=UserSerializer(read_only=True,source='registre_by')
     class Meta :
          model=Registre
          fields=['id','user_detail']


class AdsSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=SposorAds
         fields="__all__"

class ParagraphSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Paragraph
         fields= "__all__"

class VideoSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Video
         fields= "__all__"         

class QuestionSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Question
         fields= "__all__"         

class TaskFileSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=TaskFile
         fields= "__all__"         

class ImagesSreilalizer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
          if obj.image:
            return f"http://127.0.0.1:8000{obj.image.url}"
          return None
    class Meta :
         model=Images
         fields=("id","image","image_url","imagenumber","task")

class TitelSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Titel
         fields="__all__"


class TaskSreilalizer(serializers.ModelSerializer):
     images=ImagesSreilalizer(many=True,read_only=True)
     titel=TitelSreilalizer(many=True,read_only=True)
     paragraph=ParagraphSreilalizer(many=True,read_only=True)
     taskfile=TaskFileSreilalizer(many=True,read_only=True)
     question=QuestionSreilalizer(many=True,read_only=True)
     video=VideoSreilalizer(many=True,read_only=True)
     class Meta :
         model=Task
         fields="__all__"

class ChallengeRulesSerializer(serializers.ModelSerializer):
     class Meta :
         model=ChallengeRules
         fields="__all__"
              

class ChallengesSreilalizer(serializers.ModelSerializer):
        image_url = serializers.SerializerMethodField()

        def get_image_url(self, obj):
          if obj.image:
            return f"http://127.0.0.1:8000{obj.image.url}"
          return None
        registre=RegistreListSerializer(many=True,read_only=True)
        task=TaskSreilalizer(many=True,read_only=True)
        challengerule=ChallengeRulesSerializer(many=True,read_only=True)
        class Meta :
           model=Challenges
           fields=('id','name','image',"image_url",'descreption','start_date','end_date','points','is_planified','max_teamsize','challenge_type','job','challengerule','registre','task')



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



