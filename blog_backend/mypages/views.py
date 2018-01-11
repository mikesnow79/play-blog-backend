import datetime

from django.http import HttpResponse
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.datetime.now()
        context['current_time'] = now
        context['REVISION'] = '1.0.0'
        return context