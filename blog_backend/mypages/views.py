import datetime

from django.http import HttpResponse
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'

# def index_view(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)