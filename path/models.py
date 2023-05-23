from django.db import models

# Create your models here.

class LearningPath(models.Model):
    name=models.CharField(max_length=255)
    descreption=models.CharField(max_length=255,blank=True)
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    def __str__(self) -> str:
        return self.name




class GamifiedCours(models.Model):
    name=models.CharField(max_length=255)
    descreption=models.CharField(max_length=255,blank=True)
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    points=models.IntegerField()
    start_date=models.DateTimeField(null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)
    learningpath=models.ForeignKey(LearningPath,on_delete=models.CASCADE,related_name="gamifiedcours")
    def __str__(self) -> str:
        return self.name
