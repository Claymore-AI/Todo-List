from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from todo.forms import TagForm, TaskForm
from todo.models import Tag, Task
from django.views import generic


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "task_list"
    paginate_by = 3

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-created_date")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tag_list"
    paginate_by = 5


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = "http://127.0.0.1:8000/tags/create"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = "http://127.0.0.1:8000/task/create"


def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:task-list")
