from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from.models import NewUser
from rest_framework import status
from rest_framework.response import Response

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = NewUser.objects.get(email=email)
        except NewUser.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=401)
        if not user.check_password(password):
            return Response({'error': 'Invalid email or password'}, status=401)
        return Response({
            'email': user.email,
            'username': user.username,
            'role':user.role
        })


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


