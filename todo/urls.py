from django.urls import path
from .views import TodosAPIView

app_name = 'todo'

urlpatterns = [
    path('API/', TodosAPIView.as_view()),
]
