from django.test import TestCase

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
class TestListCreate(APITestCase):
    def authantiction(self,):
        data_register={'username':'ali','email':'exmple2@ex.com','password':'dddfddew@#32SD'}
        self.client.post(reverse('register'),data_register)
        
        data_login={'email':'exmple2@ex.com','password':'dddfddew@#32SD'}
        response=self.client.post(reverse('login'),data_login)
        print(response.data['token'])
        self.client.credentials(HTTP_AUTHORIZATION='Token ' +'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFsaSIsImVtYWlsIjoiZXhtcGxlMkBleC5jb20iLCJleHAiOjE3MTQ1MTM5NjJ9.FdWOkFD8iyKyU77Phn4eS-QTc7LIVjtL_CgzT-C0tX8F')
    # def test_should_not__creat_todo_with_no_auth(self): 
    #     """
    #      Test To Create Api With No Authantication  It`s Should be  forbidden
    #     """
    #     simple_to_do={'title':"Hello",'desc':"Test"}
    #     response=self.client.post(reverse('create'),simple_to_do)
    #     self.assertEqual(status.HTTP_403_FORBIDDEN,response.status_code)
    def test_should_be_crate_to_with_auth(self):
        """
        Test To Create Api With Authantication  It`s should be Successe
        """
        self.authantiction()
        simple_to_do={'title':"Hello",'desc':"Test"}
        response=self.client.post(reverse('create'),simple_to_do)
        self.assertEqual(status.HTTP_201_CREATED,response.status_code)