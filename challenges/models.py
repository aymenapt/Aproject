from django.db import models
from django.utils import timezone
from users.models import NewUser
from django.core.validators import FileExtensionValidator
from path.models import GamifiedCours
from job.models import JobOffer
# Create your models here.

class Challenges(models.Model):
    name=models.CharField(max_length=255)
    descreption=models.CharField(max_length=255,blank=True)
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    points=models.IntegerField()
    start_date=models.DateTimeField(null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)
    is_planified=models.BooleanField(default=False)
    max_teamsize=models.IntegerField(default=1)
    MY_CHOICES = (
        ('challenge', 'challenge'),
        ('job', 'job'), )
    challenge_type = models.CharField(max_length=75, choices=MY_CHOICES)
    job=models.ForeignKey(JobOffer,on_delete=models.CASCADE,null=True,blank=True,related_name="challenge")
    created_by=models.ForeignKey(NewUser,on_delete=models.CASCADE,null=True,blank=True,related_name="challenge")
    def __str__(self) -> str:
        return self.name 

class Task(models.Model):
    name=models.CharField(max_length=255)
    tasknumber=models.IntegerField()
    challenge=models.ForeignKey(Challenges,on_delete=models.CASCADE,related_name="task",null=True,blank=True)
    gamifiedcours=models.ForeignKey(GamifiedCours,on_delete=models.CASCADE,related_name="task",null=True,blank=True)
    def __str__(self) -> str:
        return self.name



class Titel(models.Model):
    titel=models.CharField(max_length=255)
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name="titel")
    titelnumber=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.titel

class Images(models.Model):
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name="images")
    imagenumber=models.IntegerField(default=0)
    

    
class Paragraph(models.Model):
    paragraph=models.CharField(max_length=600)
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name="paragraph")
    paragraphnumber=models.IntegerField(default=0)
  


class SposorAds(models.Model):
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)


class ChallengeRules(models.Model):
    rule=models.CharField(max_length=255)
    challenges=models.ForeignKey(Challenges,on_delete= models.CASCADE,related_name="challengerule")


class Registre(models.Model):
    challenge=models.ForeignKey(Challenges,on_delete=models.CASCADE,related_name="registre")
    registre_by=models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name="registre")

class Participate(models.Model):
    challenge=models.ForeignKey(Challenges,on_delete=models.CASCADE,related_name="participate")
    participate_by=models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name="participate")
    participate_result=models.IntegerField(default=0)
    finaldate_participate=models.DateTimeField(null=True,blank=True)
    class Meta:
        ordering = ('-participate_result','finaldate_participate')



class TaskFile(models.Model):
    task_file = models.FileField(upload_to='task_files/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'rar'])])
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name="taskfile")
    filenumber=models.IntegerField(default=0)

class Question(models.Model):
    question=models.CharField(max_length=800)
    question_number=models.IntegerField(default=0)
    question_point=models.IntegerField(default=0)
    question_solution=models.CharField(max_length=255)
    question_hint=models.CharField(max_length=255)
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name="question")

class Video(models.Model):
    task_vedio = models.FileField(blank=True,null=True,upload_to='task_video/', validators=[FileExtensionValidator(allowed_extensions=['mp3', 'mp4',])])
    video_number=models.IntegerField(default=0)
    task=models.ForeignKey(Task,on_delete=models.CASCADE,related_name="video")
    


class Answer(models.Model):
    answer = models.CharField(max_length=800)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name="answers")
    challenge = models.ForeignKey(Challenges, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    participate = models.ForeignKey(Participate, on_delete=models.CASCADE, related_name="answers", null=True, blank=True)