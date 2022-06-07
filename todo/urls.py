from django.urls import path
from .views import TodosAPIView, TodoGetAPIView, TodoCreateAPIView, TodoUpdateAPIView, DoneTodoAPIView

app_name = 'todo'

urlpatterns = [
    path('get/list/', TodosAPIView.as_view()),
    path('get/list/<int:pk>/', TodoGetAPIView.as_view()),
    path('post/list/', TodoCreateAPIView.as_view()),
    path('put/list/<int:pk>/', TodoUpdateAPIView.as_view()),
    path('get/done/', DoneTodoAPIView.as_view()),
]
