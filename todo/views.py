from django.views.generic import (
    # デフォルトで存在
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
# ログイン状態を確認でき、未ログイン時はログインページに遷移させる
from django.contrib.auth.mixins import LoginRequiredMixin
# URLを指定
from django.urls import reverse_lazy
from .models import Todo

from .forms import TodoForm

class IndexView(LoginRequiredMixin,ListView):
    
    template_name = 'index.html'
    model = Todo
    context_object_name = 'todos'
    
index = IndexView.as_view()


class TodoDetailView(LoginRequiredMixin,DetailView):
    
    template_name = 'todo/detail.html'
    model = Todo
    context_object_name = 'todo'
    
todo_detail = TodoDetailView.as_view()

# フォームを作成し、値を返す。
class TodoCreateView(LoginRequiredMixin,CreateView):
    
    template_name = 'todo/create.html'
    model = Todo
    form_class = TodoForm
    # 正常に入力された時の遷移先を指定
    success_url = reverse_lazy('todo:index')
    
todo_create = TodoCreateView.as_view()


class TodoUpdateView(LoginRequiredMixin,UpdateView):
    
    template_name = 'todo/update.html'
    model = Todo
    form_class = TodoForm
    success_url =  None

    def get_success_url(self):

        success_url = reverse_lazy('todo:todo_detail', kwargs={'pk':self.kwargs['pk']})
        return success_url

todo_update = TodoUpdateView.as_view()


class TodoDeleteView(LoginRequiredMixin,DeleteView):
    
    template_name = 'todo/delete.html'
    model = Todo
    success_url = reverse_lazy('todo:index')
    
todo_delete = TodoDeleteView.as_view()
