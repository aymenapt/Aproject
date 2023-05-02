from django.db import models

# Create your models here.

class Challenges(models.Model):
    name=models.CharField(max_length=255)
    descreption=models.CharField(max_length=255)
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    points=models.IntegerField()
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    name=models.CharField(max_length=255)
    tasknumber=models.IntegerField()
    challenge=models.ForeignKey(Challenges,on_delete=models.CASCADE,related_name="task")
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
  