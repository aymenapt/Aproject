from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    role = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('id','email', 'username', 'password', 'role','is_verified','image','skills')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username = attrs.get('username')
        email=attrs.get('email')
        if NewUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Sorry, the email you entered is already taken.')
    
        if NewUser.objects.filter(username=username).exists():
            raise serializers.ValidationError('Sorry, the username you entered is already taken.')
        return attrs
    
    
    def create(self, validated_data):
        user = NewUser.objects.create_user(first_name='',**validated_data)
        return user
    



class VerifyOtpSeriliezer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)
    class Meta :
        model=NewUser
        fields=('id','email', 'role', 'is_verified', 'skills', 'image', 'otp')
