import django_filters
from django.utils.translation import gettext_lazy as _
from .models import Task
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model


User = get_user_model()


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_("Status")
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_("Executor")
    )

    class Meta:
        model = Task
        fields = ['status', 'executor']
