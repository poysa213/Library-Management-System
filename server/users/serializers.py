from django.contrib.auth import authenticate
from users.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


#Serializer to Get User Details 
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "email", "phone_number"]

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
    password = serializers.CharField(
       write_only=True, required=True, validators=[validate_password])
  
    
    class Meta:
        model = User
        fields = ['phone_number', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
            
        }

    
    def create(self, validated_data):
        user = User.objects.create(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not (email and password):
            msg = 'Both "email" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        else:
            user = authenticate(request=self.context['request'], \
                email=email, password=password)

            if not user:
                msg = 'Access denied: wrong email or password.'
                raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
