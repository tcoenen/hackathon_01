from typing import Any, Dict
from django.shortcuts import render
from core.models import Process
from core.services import get_mermaid_markup

from django.views.generic import DetailView


class ProcessView(DetailView):
    model = Process
    template_name = 'core/process_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mermaid_markup'] = get_mermaid_markup(self.object.id)

        return context
