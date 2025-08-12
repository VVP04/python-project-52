from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect

from .models import Label
from .forms import LabelForm


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/index.html'
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels_index')
    success_message = _("Label created successfully")


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels_index')
    success_message = _("Label updated successfully")


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _("Label deleted successfully")
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if self.object.tasks.exists():
            messages.error(
                request,
                _("It is impossible to delete the label because it is being used")
            )
            return redirect('labels_index')
            
        return super().delete(request, *args, **kwargs)
