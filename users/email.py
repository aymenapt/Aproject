from django.core.mail import send_mail
import random 
from django.conf import settings 
from.models import NewUser


def send_otp_via_email (email):
    subject = 'Your account verfication email'
    otp=random.randint(1000,9999)
    message=f'Your otp is {otp}'
    email_from =settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email] )
    user_obj= NewUser.objects.get(email=email)
    user_obj.otp=otp
    user_obj.save()

def sendinterview (email,interviewlink,interviewdate,descreption):
    subject = 'Congratulations! Interview Details and Link Enclosed'
    message = f""" 
        {descreption} 
        Interview Date : {interviewdate}
        Interview Link : {interviewlink}
    """
       


    email_from =settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email])


def restpassword (email,password):
      subject = 'Your Password Recovery'
      message=f'Your password  is : {password}'
      email_from =settings.EMAIL_HOST_USER
      send_mail(subject, message, email_from, [email] )