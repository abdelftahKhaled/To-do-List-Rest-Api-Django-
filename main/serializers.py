from rest_framework import serializers
from main.models import todo 

class ToDo_Serilizer(serializers.ModelSerializer):
    
    class Meta :
        model=todo
        fields=['is_complete','title','desc','owner']
        read_only_fields=['owner',]
class ListToDoSerilizer(serializers.ModelSerializer)    :
    class Meta:
        model=todo
        fields='__all__'    