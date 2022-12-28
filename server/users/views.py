from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import permissions

from rest_framework import status
from rest_framework import views, generics
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer



class RegisterUserAPIView(generics.CreateAPIView):
  serializer_class = RegisterSerializer
  permission_classes = (permissions.AllowAny,)
  
  

class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)



# Class based view to Get User Details using Token Authentication
class UserDetailAPI(views.APIView):
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)