from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer,VerifyOtpSeriliezer,UpdateUserSerializer
from rest_framework.permissions import AllowAny
from.models import NewUser
from rest_framework import status
from rest_framework.response import Response
from.email import send_otp_via_email
from django.utils import timezone
from datetime import timedelta



class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = NewUser.objects.get(email=email)
            bancount=user.bancount
        except NewUser.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if user.is_verified == False :
                 return Response({'error': 'This account must be verified'}, status=status.HTTP_401_UNAUTHORIZED)


        if user.bancount ==3 :
            bancount =bancount+1
            user.bancount= bancount
            user.is_baned = True
            user.baned_time=timezone.now()+timedelta(minutes=2)
            user.save()
           
            print(user.baned_time)
        
        if timezone.now() > user.baned_time :
            user.is_baned = False
            user.bancount = 0
            user.save()
            print(user.bancount)

        if user.is_baned :
             return Response({'error': 'this account baned for 2 min'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            bancount =bancount+1
            user.bancount= bancount
            user.save()
            print(user.bancount)

            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
      

        serialzer=CustomUserSerializer(user)
        return Response({
                    'data':serialzer.data
                      },
                      status=status.HTTP_200_OK
                      )


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_otp_via_email(serializer.data['email'])

            if user:
                json = serializer.data
                return Response({
                    'message': 'regestration succesfuly check email',
                    'data': json, },
                    status=status.HTTP_200_OK
                    )
                                 
            
        return Response({
                    'message':'somthing went wrong' ,
                    'data':serializer.errors },
                    status=status.HTTP_400_BAD_REQUEST

                    )
                             


class Verifyotp(APIView):
    def post(self, request):
        serializer = VerifyOtpSeriliezer(request.data)
        email = serializer.data['email']
        otp = serializer.data['otp']
        user_queryset = NewUser.objects.all().filter(email=email)
         
        if not user_queryset.exists():
            return Response({
                    
                    'message': 'invalid email',
                     },
                     status=status.HTTP_400_BAD_REQUEST
                     )
        
        user = user_queryset.first()
        if user.otp != otp:
            return Response({
                  
                    'message': 'wrong otp',
                     },
                     status=status.HTTP_400_BAD_REQUEST
                     )
        

        user.is_verified = True
        user.save()
        
        return Response({
                   
                    'message': 'email verified',
                    'email': user.email,
                    'username': user.username,
                    'is_verified': user.is_verified,
                    'role': user.role,
                    'skills': user.skills,
                     },
                     status=status.HTTP_200_OK
                     )

        
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UpdateUserSerializer
    lookup_field = 'id'

class UserDelete(generics.DestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserCreate
    lookup_field = 'id'


        
