from django.urls import path
from .views import create,list,list_create,retrive_update_delete
urlpatterns = [
    path('create',create,name='create'),
    path('list',list,name='list'),
    path('list_create',list_create,name='list_create'),
    path('retrive_update_delete/<int:id>',retrive_update_delete,name='retrive_update_delete'),
    
]
