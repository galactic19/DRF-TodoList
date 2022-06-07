from django.urls import path
from .views import TodosAPIView, TodoGetAPIView

app_name = 'todo'

urlpatterns = [
    path('GET/', TodosAPIView.as_view()),
    path('GET/<int:pk>/', TodoGetAPIView.as_view()),
]
