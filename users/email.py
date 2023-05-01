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

