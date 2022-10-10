from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_create.html'
    success_url = reverse_lazy('todo_create')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo_delete.html"
    success_url = reverse_lazy('todo_list')
