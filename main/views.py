from django.shortcuts import render
from .models import todo
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ToDo_Serilizer,ListToDoSerilizer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions,filters
from .pagination import customPageNumberPagnation

class CreatTodo(CreateAPIView):
    serializer_class=ToDo_Serilizer
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    permission_classes=[IsAuthenticated]



class List_Todo(ListAPIView):
    serializer_class=ToDo_Serilizer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['id','title','is_complete','desc']
    search_fields=['id','title','is_complete','desc']
    ordering_fields=['id','title','is_complete','desc']
    pagination_class=customPageNumberPagnation
    
    def get_queryset(self):
        return todo.objects.filter(owner=self.request.user)
    
class List_create(ListCreateAPIView):
        serializer_class=ToDo_Serilizer
        def get_queryset(self):
            return todo.objects.filter(owner=self.request.user)
        def perform_create(self, serializer):
           return serializer.save(owner=self.request.user)
class Retrive_update_delete(RetrieveUpdateDestroyAPIView):
        serializer_class=ToDo_Serilizer
        lookup_field='id'
        def get_queryset(self):
            return todo.objects.filter(owner=self.request.user)
       
list=List_Todo().as_view()
create=CreatTodo().as_view()
list_create=List_create.as_view()
retrive_update_delete=Retrive_update_delete().as_view()