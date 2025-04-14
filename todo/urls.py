from django.urls import path

from todo.views import (
    TaskListView,
    toggle_task_status,
    TagListView,
    TagCreateView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "todo"
urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
    path("chng_st/<int:task_id>", toggle_task_status, name="toggle-task-status"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
]
