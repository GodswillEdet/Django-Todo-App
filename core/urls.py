from django.urls import path

from .views import TodoListView, TodoCreateView, TodoDeleteView
urlpatterns = [
    path('tasks/', TodoListView.as_view(), name='todo_list'),
    path('', TodoCreateView.as_view(), name='todo_create'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete')
]
