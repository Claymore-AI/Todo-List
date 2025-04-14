from django import forms
from django.db.models import QuerySet
from todo.models import Task, Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    tags_queryset: QuerySet = Tag.objects.all()

    tags = forms.ModelMultipleChoiceField(
        queryset=tags_queryset, widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
