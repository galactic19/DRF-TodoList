from rest_framework import serializers
from .models import Todo


class TodoSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('pk', 'title', 'complete', 'important')
        
        
class TodoDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('pk', 'title', 'description', 'creaeted', 'complete', 'important')


class TodoCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')