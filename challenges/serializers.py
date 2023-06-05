from django.conf import settings
from rest_framework import serializers 
from.models import *
from users.models import NewUser


class UserSerializer(serializers.ModelSerializer):
     class Meta :
          model=NewUser
          fields=['id','email', 'username','point']
     


class RegistreSerializer(serializers.ModelSerializer):
     class Meta :
          model=Registre
          fields=['id','registre_by','challenge']

class AnswerSerializer(serializers.ModelSerializer):
     class Meta:
        model = Answer
        fields = ['answer','question','user','challenge','participate'] 

class ParticipateSerializer(serializers.ModelSerializer):
     answers = AnswerSerializer(many=True,read_only=True)
     class Meta :
          model=Participate
          fields=['id','participate_by','challenge','participate_result','answers']

class RegistreListSerializer(serializers.ModelSerializer):
     user_detail=UserSerializer(read_only=True,source='registre_by')
     class Meta :
          model=Registre
          fields=['id','user_detail']

      

class ParticipateListSerializer(serializers.ModelSerializer):
     answers = AnswerSerializer(many=True,read_only=True)
     user_detail=UserSerializer(read_only=True,source='participate_by')
     class Meta :
          model=Participate
          fields=['id','user_detail','participate_result','answers']

class AdsSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=SposorAds
         fields="__all__"

class ParagraphSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Paragraph
         fields= "__all__"

class UpdateParagraphSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Paragraph
         fields= "__all__"
         extra_kwargs = {
            'paragraph': {'required': False},
            'task': {'required': False},
            'paragraphnumber': {'required': False},
        }       

class VideoSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Video
         fields= "__all__"     

class UpdateVideoSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Video
         fields= "__all__"
         extra_kwargs = {
            'task_vedio': {'required': False},
            'task': {'required': False},
            'video_number': {'required': False},
        }    

class QuestionSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Question
         fields= "__all__"    

class UpdateQuestionSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Question
         fields= "__all__"
         extra_kwargs = {
            'question': {'required': False},
            'task': {'required': False},
            'question_number': {'required': False},
            'question_point': {'required': False},
            'question_solution': {'required': False},
            'question_hint': {'required': False},
        }

class TaskFileSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=TaskFile
         fields= "__all__"         

class UpdateFileSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=TaskFile
         fields= "__all__"
         extra_kwargs = {
            'task_file': {'required': False},
            'task': {'required': False},
            'filenumber': {'required': False},
        }             

class ImagesSreilalizer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
          if obj.image:
            return f"http://127.0.0.1:8000{obj.image.url}"
          return None
    class Meta :
         model=Images
         fields=("id","image","image_url","imagenumber","task")

class UpdateImagesSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Images
         fields= "__all__"
         extra_kwargs = {
            'image': {'required': False},
            'task': {'required': False},
            'imagenumber': {'required': False},
        } 
class TitelSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Titel
         fields="__all__"


class UpdateTitelSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Titel
         fields= "__all__"
         extra_kwargs = {
            'titel': {'required': False},
            'task': {'required': False},
            'titelnumber': {'required': False},
        } 

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


class UpdateTaskSreilalizer(serializers.ModelSerializer):
    class Meta :
         model=Task
         fields= "__all__"
         extra_kwargs = {
            'images': {'required': False},
            'titel': {'required': False},
            'paragraph': {'required': False},
            'taskfile': {'required': False},
            'question': {'required': False},
            'video': {'required': False},
            'tasknumber': {'required': False},
            'challenge': {'required': False},
            'gamifiedcours': {'required': False},
        }   


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
        participate=ParticipateListSerializer(many=True,read_only=True)
        task=TaskSreilalizer(many=True,read_only=True)
        challengerule=ChallengeRulesSerializer(many=True,read_only=True)
        class Meta :
           model=Challenges
           fields=('id','name','image',"image_url",'descreption','created_by','start_date','end_date','points','is_planified','max_teamsize','challenge_type','job','challengerule','registre','participate','task')



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




