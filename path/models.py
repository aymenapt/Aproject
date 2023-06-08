from django.db import models
from users.models import NewUser

# Create your models here.

class LearningPath(models.Model):
    name=models.CharField(max_length=255)
    descreption=models.CharField(max_length=255,blank=True)
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_by=models.ForeignKey(NewUser,on_delete=models.CASCADE,null=True,blank=True,related_name="learningpath")
    def __str__(self) -> str:
        return self.name



class GamifiedCours(models.Model):
    name=models.CharField(max_length=255)
    descreption=models.CharField(max_length=255,blank=True)
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    learningpath=models.ForeignKey(LearningPath,on_delete=models.CASCADE,related_name="gamifiedcours")
    def __str__(self) -> str:
        return self.name

class GamifiedCoursParticipate(models.Model):
    gamifiedcours=models.ForeignKey(GamifiedCours,on_delete=models.CASCADE,related_name="coursparticipate",null=True,blank=True)
    participate_by=models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name="coursparticipate")
    participate_result=models.IntegerField(default=0)
    finaldate_participate=models.DateTimeField(null=True,blank=True)
    class Meta:
        ordering = ('-participate_result','finaldate_participate')




