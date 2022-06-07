from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Todo
from .serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer

class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
    # def post(self, request):
    #     serializer = TodoCreateSerializer(data=request.data)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
      
    
class TodoGetAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class TodoCreateAPIView(APIView):
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class TodoUpdateAPIView(APIView):
    def put(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoCreateSerializer(todo, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)