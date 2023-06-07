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

def sendinterview (email,interviewlink):
    subject = 'Congratulations! Interview Details and Link Enclosed'
    message = f'Dear participant, We are absolutely thrilled to announce that you have emerged as the winner of the job offer challenge. Congratulations on your outstanding achievement! Your talent and dedication have truly set you apart from the competition.In recognition of your remarkable accomplishment, we would like to invite you for an interview to discuss your victory and explore further opportunities. To access the interview, simply click on the following link: {interviewlink}. This will lead you to the virtual meeting room where our team will be waiting to engage in an insightful discussion with you.During the interview, we will delve into your experiences, aspirations, and how you can contribute to our company. We encourage you to come prepared with any questions you may have for us.If you have any scheduling conflicts or require any accommodations, please let us know as soon as possible, and we will make every effort to accommodate your needs.Once again, congratulations on your well-deserved victory! We are excited to connect with you and learn more about your exceptional talents.Should you have any inquiries or need further information, please do not hesitate to contact us. Best regards'


    email_from =settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email])


def restpassword (email,password):
      subject = 'Your Password Recovery'
      message=f'Your password  is : {password}'
      email_from =settings.EMAIL_HOST_USER
      send_mail(subject, message, email_from, [email] )