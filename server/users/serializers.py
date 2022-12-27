from django.contrib.auth import authenticate
from rest_framework import serializers



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, label="Username")
    password = serializers.CharField(write_only=True, label="Username")

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not (username and password):
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        else:
            user = authenticate(request=self.context['request'], \
                username=username, password=password)

            if not user:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
