
from rest_framework.generics import GenericAPIView
from authantiction.serializers import RegisterSerializers ,LoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status
from django.contrib.auth import authenticate
from rest_framework import exceptions

class RegisterApiViwe(GenericAPIView):
    serializer_class=RegisterSerializers
    def post(self,request,):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(data=serializer.data,status=status.HTTP_201_CREATED)  
        return response.Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class LoginApiViwe(GenericAPIView):
    serializer_class =LoginSerializer 
    def post(self,request):
            email=request.data['email']
            password=request.data['password']
            user=authenticate(email=email,password=password)
            
            if user:
                
                serializer=self.serializer_class(instance=user)
                

                return response.Response(data=serializer.data,status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
class Profile_User(GenericAPIView):
   serializer_class =RegisterSerializers
   permission_classes=[IsAuthenticated]
   def get(self,request):
        user=request.user
        serializer=self.serializer_class(instance=user)
        return response.Response({'user':serializer})

login=LoginApiViwe.as_view()
register=RegisterApiViwe.as_view()