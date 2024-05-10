import jwt 
from authantiction.models import User
import jwt.exceptions
from rest_framework.authentication import get_authorization_header,BaseAuthentication
from rest_framework import exceptions
class jwtAuthanticate(BaseAuthentication):
    def authenticate(self, request):
        auth_header=get_authorization_header(request)
  
        auth_data=auth_header.decode('utf-8')
        auth_token=auth_data.split(" ")

        print(auth_token)
        if len(auth_token)>2:
            raise exceptions.AuthenticationFailed()
        token=auth_token[1]
        try :
            
            from django.conf import settings
            pyload=jwt.decode(token,settings.SECRET_KEY,'HS256')
            username=pyload['username']
            email=pyload['email']
            user=User.objects.get(email=email,username=username)
            return (user,token)
        except jwt.exceptions.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed('Token is expired , login again')
        except User.DoesNotExist as No_user :
            raise exceptions.AuthenticationFailed('User is not Exsist')
        except jwt.exceptions.DecodeError as ex:
            raise exceptions.AuthenticationFailed('error in decodeing token')
        
        
   
    
    
    
    