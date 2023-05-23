from django.db import models

# Create your models here.

class JobOffer(models.Model):
    name=models.CharField(max_length=255)
    descreption=models.CharField(max_length=800,blank=True)
    skillsrequirment=models.CharField(max_length=800,blank=True)
    jobbenifits=models.CharField(max_length=800,blank=True)
    employment_nedded=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name